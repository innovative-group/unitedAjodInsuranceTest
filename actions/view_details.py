from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionViewDetails(Action):

    def name(self) -> Text:
        return "action_view_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        details = tracker.get_slot("details")          # --------------> here "details" is entities
        form_type = tracker.get_slot("form_type")

        if form_type == "policy detail form":
            try:
                with open('actions/responses/view_details.json', 'r') as f:
                    data = json.load(f)
                    response = data.get('policy_detail_form')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif form_type == "personal detail form":
            try:
                with open('actions/responses/view_details.json', 'r') as f:
                    data = json.load(f)
                    response = data.get('personal_detail_form')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        if details == "policy details":
            dispatcher.utter_message(
                text=f"Please click the button below and provide the details to view your policy details.",
                buttons=[{
                    "title": "View Policy Details",
                    "payload": f"/view_details{{\"form_type\":\"policy detail form\"}}"
                }]
            )
            return[]

        elif details == "personal details":
            dispatcher.utter_message(
                text=f"Please click the button below and provide the details to view your personal details.",
                buttons=[{
                    "title": "View Personal Details",
                    "payload": f"/view_details{{\"form_type\":\"personal detail form\"}}"
                }]
            )
            return[]

        else:
            dispatcher.utter_message(
                text=f"Please click the buttons below to view your details.",
                buttons=[
                    {
                        "title": "View Policy Details",
                        "payload": f"/view_details{{\"form_type\":\"policy detail form\"}}"
                        
                    },
                    {
                        "title": "View Personal Details",
                        "payload": f"/view_details{{\"form_type\":\"personal detail form\"}}"
                    }
                ]
            )
            return[]


# here: view_details --> is an "intent"
# here: form_type:   --> is an "entities"