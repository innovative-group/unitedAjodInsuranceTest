from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionPurchase(Action):

    def name(self) -> Text:
        return "action_purchase"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        document = tracker.get_slot("document")
        print("value of [action_purchase] document= ", document)

        if document == "form":

            try:
                with open('actions/responses/purchase_form.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('interestForm')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        else:
            dispatcher.utter_message(
                text=f"Please fill up the given form to purchase a policy from us.",
                buttons=[
                    {
                        "title": "Insurance Purchase Form",
                        "payload": f"/purchase{{\"document\":\"form\"}}"
                    }
                ]
            )
            return[]
