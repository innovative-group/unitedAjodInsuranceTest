from typing import Any, Dict, List, Optional, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import SlotSet, AllSlotsReset


class Careers(Action):
    def name(self) -> Text:
        return "action_careers"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        company_info = tracker.get_slot("company_info")

        link = "https://unitedajodinsurance.com/about-us"

        if company_info == "vacancy":
            dispatcher.utter_message(
                text=f"Visit our careers page to know about current job openings.",
                buttons=[{"title": "Careers",
                          "link": link}]
            )

        else:
            dispatcher.utter_message(
                text=f"We kindly request you to visit our careers page for more information.",
                buttons=[{"title": "Careers",
                          "link": link}]
            )

        return[]
