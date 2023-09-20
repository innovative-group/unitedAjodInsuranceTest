from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionDownloads(Action):

    def name(self) -> Text:
        return "action_downloads"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        form_type = tracker.get_slot("form_type")

        if form_type == "kyc":
            dispatcher.utter_message(
                text=f"Please click the button below to download the KYC form.",
                buttons=[
                    {"title": "KYC forms",
                     "link": "https://siddharthapremier.com.np/pages?id=29"
                     }
                ]
            )
            return[]

        elif form_type == "proposal":
            dispatcher.utter_message(
                text=f"Please click the button below to download the proposal form.",
                buttons=[{
                    "title": "Proposal forms",
                    "link": "https://siddharthapremier.com.np/pages?id=18"
                }]
            )
            return[]

        elif form_type == "claim":
            dispatcher.utter_message(
                text=f"Please click the button below to download the claim form.",
                buttons=[{
                    "title": "Claim Forms",
                    "link": "https://siddharthapremier.com.np/pages?id=90"
                }]
            )
            return[]

        else:
            dispatcher.utter_message(
                text=f"Please click the button below to download the forms.",
                buttons=[{
                    "title": "KYC forms",
                    "link": "https://siddharthapremier.com.np/pages?id=29"
                },
                    {
                    "title": "Proposal forms",
                    "link": "https://siddharthapremier.com.np/pages?id=18"
                },
                    {
                    "title": "Claim Forms",
                    "link": "https://siddharthapremier.com.np/pages?id=90"
                }
                ]
            )
            return[]
