from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionFeedback(Action):

    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        feedback_type = tracker.get_slot("feedback_type")
        document = tracker.get_slot("document")

        if document == "form":
            if feedback_type == "feedback":
                try:
                    with open('actions/responses/feedback.json', 'r') as f:
                        data = json.load(f)
                        response = data.get('feedback')
                        dispatcher.utter_message(json_message=response)
                except Exception as error:
                    print(error)
                return[]

            elif feedback_type == "complain":
                try:
                    with open('actions/responses/feedback.json', 'r') as f:
                        data = json.load(f)
                        response = data.get('complain')
                        dispatcher.utter_message(json_message=response)
                except Exception as error:
                    print(error)
                return[]

        if feedback_type == "feedback":
            dispatcher.utter_message(
                text=f"Please fill up the given form to provide your valuable feedback.",
                buttons=[
                    {"title": "Feedback",
                     "payload": f"/feedback{{\"document\":\"form\",\"feedback_type\":\"feedback\"}}"}
                ])
            return[]

        elif feedback_type == "complain":
            dispatcher.utter_message(
                text=f"Please fill up the given form to register your complain.",
                buttons=[
                    {
                        "title": "Complain",
                        "payload": f"/feedback{{\"document\":\"form\",\"feedback_type\":\"complain\"}}"
                    }
                ])

        else:
            buttons = [
                {"title": "Feedback",
                 "payload": f"/feedback{{\"document\":\"form\",\"feedback_type\":\"feedback\"}}"},
                {"title": "Complain",
                 "payload": f"/feedback{{\"document\":\"form\",\"feedback_type\":\"complain\"}}"}]

            dispatcher.utter_message(
                text=f"Please click the buttons below to register your complain/feedback.",
                buttons=buttons
            )
            return[]


