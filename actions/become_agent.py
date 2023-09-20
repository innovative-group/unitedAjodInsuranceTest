from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import AllSlotsReset


class ActionBecomeAgent(Action):

    def name(self) -> Text:
        return "action_become_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_type = tracker.get_slot("user_type")
        if user_type == "agent":
            try:
                with open('actions/responses/become_agent.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('become_agent')

                    dispatcher.utter_message(json_message=response)
                    return []
            except Exception as error:
                print(error)
            return[]
