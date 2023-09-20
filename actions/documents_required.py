from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionDocumentsRequired(Action):

    def name(self) -> Text:
        return "action_documents_required"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_type = tracker.get_slot("product_type")

        insurance_info = tracker.get_slot("insurance_info")

        if insurance_info == "purchase":
            # if product_type == "child":
            try:
                with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                    data = json.load(f)
                    response = data.get('purchase_insurance')
                    dispatcher.utter_message(json_message=response)

            except Exception as error:
                print(error)
            return[]

        elif insurance_info == "claim":
            if product_type == "engineering":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('engineering_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "third party":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('third_party_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "passenger death":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('passenger_death_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "micro insurance":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('micro_insurance_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "fire":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('fire_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "marine":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('marine_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "theft vehicle":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('theft_vehicle_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            elif product_type == "pa/gpa/md":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('pa/gpa/md_claim')
                        dispatcher.utter_message(json_message=response)
                except Exception as error:
                    print(error)
                return[]

            elif product_type == "motor":
                try:
                    with open('actions/responses/documents_required.json', 'r', encoding="utf8") as f:
                        data = json.load(f)
                        response = data.get('motor_claim')
                        dispatcher.utter_message(json_message=response)

                except Exception as error:
                    print(error)
                return[]

            else:
                dispatcher.utter_message(
                    text=f"Please choose the options from below:",
                    buttons=[
                        {
                            "title": "Engineering Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"engineering\"}}"
                        },
                        {
                            "title": "Third Party Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"third party\"}}"
                        },
                        {
                            "title": "Passenger Death Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"passenger death\"}}"
                        },
                        {
                            "title": "Micro Insurance Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"micro insurance\"}}"
                        },
                        {
                            "title": "Fire Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"fire\"}}"
                        },
                        {
                            "title": "Marine Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"marine\"}}"
                        },
                        {
                            "title": "Theft Vehicle Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"theft vehicle\"}}"
                        },
                        {
                            "title": "PA/GPA/MD Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"pa/gpa/md\"}}"
                        },
                        {
                            "title": "Motor Claim",
                            "payload": f"/documents_required{{\"insurance_info\":\"claim\", \"product_type\":\"motor\"}}"
                        }
                    ]
                )
                return[]

        else:
            dispatcher.utter_message(
                text=f"Please click the buttons below to know about the documents required for:",
                buttons=[
                    {
                        "title": "Claim Insurance",
                        "payload": f"/documents_required{{\"insurance_info\":\"claim\"}}"
                    },
                    {
                        "title": "Purchase Insurance",
                        "payload": f"/documents_required{{\"insurance_info\":\"purchase\"}}"
                    }
                ]
            )

            return[]
