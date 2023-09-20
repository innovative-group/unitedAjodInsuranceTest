from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionHospitalList(Action):

    def name(self) -> Text:
        return "action_hospital_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            with open('actions/responses/hospital_list.json', 'r', encoding='utf8') as f:
                data = json.load(f)
                response = data.get('hospital_list')
                print("I am in hospital list.")
                print(response)
                dispatcher.utter_message(json_message=response)
        except Exception as error:
            print(error)
        return[]
