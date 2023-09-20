from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionProcedure(Action):

    def name(self) -> Text:
        return "action_procedure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        insurance_info = tracker.get_slot("insurance_info")

        if insurance_info == "claim":
            try:
                with open('actions/responses/procedure.json', 'r', encoding='utf-8') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('claim_process')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)

            return[]

        elif insurance_info == "purchase":
            try:
                with open('actions/responses/procedure.json', 'r', encoding='utf-8') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('purchase_process')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)

            return[]

        else:
            dispatcher.utter_message(
                text=f"Please choose from the options below:",
                buttons=[
                    {
                        "title": "Claim Process",
                        "payload": f"/procedure{{\"insurance_info\":\"claim\"}}"
                    },
                    {
                        "title": "Purchase Process",
                        "payload": f"/procedure{{\"insurance_info\":\"purchase\"}}"
                    }
                ]
            )
            return[]
