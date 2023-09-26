from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionProcedure(Action):

    def name(self) -> Text:
        return "action_claim/purchase_procedure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        procedure_for = tracker.get_slot("procedure_for")
        print("\n\n -------->> ", procedure_for, "<<----------\n\n")
        if procedure_for == "claim":
            try:
                with open('actions/responses/claim_or_purchase_procedure.json', 'r', encoding='utf-8') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('insurance_claim_procedure')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)

            return[]

        elif procedure_for == "purchase":
            try:
                with open('actions/responses/claim_or_purchase_procedure.json', 'r', encoding='utf-8') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('insurance_purchase_Procedure')
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
                        "payload": f"/claim_or_purchase_procedure{{\"procedure_for\":\"claim\"}}"
                    },
                    {
                        "title": "Purchase Process",
                        "payload": f"/claim_or_purchase_procedure{{\"procedure_for\":\"purchase\"}}"
                    }
                ]
            )
            return[]
