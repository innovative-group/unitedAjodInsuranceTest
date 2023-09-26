from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionProductInfo(Action):

    def name(self) -> Text:
        return "action_product_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_type = tracker.get_slot("product_type")
    

        if product_type == "property":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('property')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif product_type == "motor":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('motor')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        

                

        elif product_type == "marine":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('marine')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif product_type == "miscellaneous":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('miscellaneous')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif product_type == "travelMedical":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('travelMedical')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif product_type == "engineering":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('engineering')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        

        elif product_type == "agriculture":
            try:
                with open('actions/responses/product_info.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('agriculture')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]       
         
 
        else:
            buttons = [

                {"title": "Property Insurance",
                    "payload": f"/product_info{{\"product_type\":\"property\"}}"},
                
                {"title": "Motor Insurance",
                    "payload": f"/product_info{{\"product_type\":\"motor\"}}"},
                
                {"title": "Marine Insurance",
                    "payload": f"/product_info{{\"product_type\":\"marine\"}}"},
                
                {"title": "Miscellaneous Insurance",
                    "payload": f"/product_info{{\"product_type\":\"miscellaneous\"}}"},
        
                {"title": "Travel Medical Insurance",
                    "payload": f"/product_info{{\"product_type\":\"travelMedical\"}}"},
        

                {"title": "Engineering Insurance",
                    "payload": f"/product_info{{\"product_type\":\"engineering\"}}"},

                {"title": "Agriculture Insurance",
                    "payload": f"/product_info{{\"product_type\":\"agriculture\"}}"},
                                        
                
            ]

            dispatcher.utter_message(
                text="Please select the product type you are interested in.",
                buttons=buttons
            )
            return[]
