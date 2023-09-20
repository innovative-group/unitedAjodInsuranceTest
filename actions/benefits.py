from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import AllSlotsReset


class ActionBenefits(Action):

    def name(self) -> Text:
        return "action_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_type = tracker.get_slot("product_type")

        if product_type == "health":
            dispatcher.utter_message(
                text=f"In case of health insurance, financial help is provided at the time of a medical emergency.",
                buttons=[
                    {
                        "title": "Health Insurance",
                        "payload": f"/product_info{{\"product_type\":\"health\"}}"
                    }
                ]
            )
            return[]

        elif product_type == "motor":
            dispatcher.utter_message(
                text=f"It is mandatory by law to buy a third-party motor insurance policy. It can take care of the compensation to be paid to the third party in case of damage to property or life.",
                buttons=[
                    {
                        "title": "Motor Insurance",
                        "payload": f"/product_info{{\"product_type\":\"motor\"}}"
                    }
                ]
            )
            return[]

        elif product_type == "property":
            dispatcher.utter_message(
                text=f"Property insurance covers the property of the policyholder against many unforeseen incidents, like fire, burglary, natural calamities, riots, etc.",
                buttons=[
                    {
                        "title": "Property Insurance",
                        "payload":  f"/product_info{{\"product_type\":\"property\"}}"
                    }
                ]
            )
            return[]

        else:
            try:
                with open('actions/responses/benefits.json', 'r') as f:
                    data = json.load(f)
                    response = data.get('benefits')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
