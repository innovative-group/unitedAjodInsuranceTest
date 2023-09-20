from dotenv import load_dotenv, find_dotenv
import pandas as pd
import json
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, FollowupAction
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rasa_sdk.events import UserUtteranceReverted
import logging
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())
model_name = os.getenv("MODEL_NAME")
use_auth_token = os.getenv('MODEL_TOKEN')


class Searcher():
    def __init__(self):
        self.model = SentenceTransformer(
            model_name, use_auth_token=use_auth_token)
        self.new_df = None

    def get_embedding(self, dataset):
        embeddings = [
                      self.model.encode(dataset['question'][i])
                      for i in range(len(dataset['question']))
                      
                      ]
        self.new_df = pd.concat([dataset, pd.DataFrame(embeddings)], axis=1)
        return self.new_df

    def get_answer(self, user_input, top_k=5):
        user_input_embedding = self.model.encode(user_input)
        similarity_scores = self.new_df.iloc[:, 3:].apply(
            lambda x: cosine_similarity([user_input_embedding], [x])[0][0], axis=1)
        top_k_indices = similarity_scores.nlargest(top_k).index.tolist()
        score = []
        question = []
        answer = []
        for idx in top_k_indices:
            score.append(similarity_scores[idx])
            question.append(self.new_df.loc[idx]['question'])
            answer.append(self.new_df.loc[idx]['answer'])
        result = pd.DataFrame(zip(question, answer, score), columns=[
                              'question', 'answer', 'score'])
        return result


searcher = Searcher()
dataset = pd.read_excel("data/nlu/responses/faq.xlsx")
embedded_data = searcher.get_embedding(dataset)


class ActionFaq(Action):
    def name(self) -> Text:
        return "action_faq"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # get user query
            query = tracker.latest_message.get("text")
            result = searcher.get_answer(query)
            max_score_index = result['score'].idxmax()
            row_with_max_score = result.iloc[max_score_index]
            # print("result",result)
            # print("row_with_max_score",row_with_max_score)

            if max(result['score']) < 0.5:
                button = {
                    "title": "Sorry I could not understand. Please rephrase. Alternatively contact us or get a callback.",
                    "type": "quick_reply",
                    "multi": True,
                    "data": [
                        {
                            'title': 'Contact to our Office',
                            'payload': '/contact'
                        },
                        {
                            'title': "Get a callback from us",
                            'payload': '/callback'
                        }
                    ]
                }
                dispatcher.utter_message(json_message=button)
                return []

            if row_with_max_score['score'] > 0.8:
                dispatcher.utter_message(
                    text=f"{row_with_max_score['answer']}")
                return []

            else:
                listDescription = {
                    "title": "Sorry I didn't understand. Did you mean:",
                    "type": "ListItem",
                    "multi": True,
                    "data": [

                    ]
                }

                for i in range(len(result['question'])):
                    listDescription.get("data").append(
                        {
                            "subtitle": result['question'][i],
                            "subdata": {
                                "detail": result['answer'][i],
                            },
                        },
                    )

                listDescription.update({
                    "button": [
                        {
                            'title': 'Contact to our Office',
                            'payload': '/contact'
                        },
                        {
                            'title': "Get a callback from us",
                            'payload': '/callback'
                        }
                    ]
                }
                )
                # # print(listDescription)
                dispatcher.utter_message(json_message=listDescription)
                return []

        except Exception as e:
            print("exception", e)
