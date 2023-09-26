from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json



class ActionPremiumCalculation(Action):

    def name(self) -> Text:
        return "action_premium_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_type = tracker.get_slot("product_type")
        calculation_type = tracker.get_slot("calculation_type")

        if product_type == "motorbike":
            print("I am inside motorbike")
            if calculation_type == "third party":
                try:
                    with open('actions/responses/premium_calculation.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('bikeThirdParty')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif calculation_type == "comprehensive":
                try:
                    with open('actions/responses/premium_calculation.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('bikeComprehensive')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            else:
                dispatcher.utter_message(
                    text=f"Please select the options below for Third Party or Comprehensive (Full Coverage) for Motor Bike insurance.",
                    buttons=[
                        {
                            "title": "Third Party",
                            "payload": f"/premium_calculation{{\"product_type\":\"motorbike\", \"calculation_type\":\"third party\"}}"
                        },
                        {
                            "title": "Comprehensive",
                            "payload": f"/premium_calculation{{\"product_type\":\"motorbike\", \"calculation_type\":\"comprehensive\"}}"
                        }
                    ]
                )
                return[]

        elif product_type == "private_vehicle":
            if calculation_type == "third party":
                try:
                    with open('actions/responses/premium_calculation.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get(
                            'privateVehicleThirdParty')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif calculation_type == "comprehensive":
                try:
                    with open('actions/responses/premium_calculation.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get(
                            'privateVehicleComprehensive')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            else:
                dispatcher.utter_message(
                    text=f"Please select the options below for Third Party or Comprehensive (Full Coverage) for Private Vehicle insurance.",
                    buttons=[
                        {
                            "title": "Third Party",
                            "payload": f"/premium_calculation{{\"product_type\":\"private vehicle\", \"calculation_type\":\"third party\"}}"
                        },
                        {
                            "title": "Comprehensive",
                            "payload": f"/premium_calculation{{\"product_type\":\"private vehicle\", \"calculation_type\":\"comprehensive\"}}"
                        }
                    ]
                )
                return[]
        
        else:
            dispatcher.utter_message(
                text=f"Please choose the options below to calculate premium.",
                buttons=[
                    {
                        "title": "Motorbikes",
                        "payload": f"/premium_calculation{{\"product_type\":\"motorbike\"}}"
                    },
                    {
                        "title": "Private Vehicles",
                        "payload": f"/premium_calculation{{\"product_type\":\"private vehicle\"}}"
                    },
              
                ]
            )
            return[]
