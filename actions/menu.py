from typing import Any, Dict, List, Optional, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import AllSlotsReset


class ActionMenu(Action):
    def name(self) -> Text:
        return "action_menu"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        try:
            with open('actions/responses/menu.json', 'r', encoding='utf8') as f:
                data = json.load(f)
                print("I am inside menu ko json")
                response = data.get('menu')
                dispatcher.utter_message(json_message=response)
        except Exception as error:
            print(error)
        return[]


class ResetSlots(Action):
    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
