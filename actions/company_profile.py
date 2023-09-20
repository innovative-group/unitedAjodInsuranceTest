from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionCompanyProfile(Action):

    def name(self) -> Text:
        return "action_company_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        company_info = tracker.get_slot("company_info")

        if company_info == "ceo":
            dispatcher.utter_message(
                text=f"Mr.Shrawan Rawal is the ceo of United Ajod Insurance Company."
            )
            return[]

        elif company_info == "information officer":
            dispatcher.utter_message(
                text=f"Mr. B.P. Upadhyay is the information officer of United Ajod Insurance company. You can call him at 977-01-5343072 or email him at baidyanath@unitedajodinsurance.com"
            )
            return[]

        elif company_info == "board of directors":
            dispatcher.utter_message(
                text=f"Click the button below to view our board of directors.",
                buttons=[
                    {"title": "Board of Directors",
                     "link": "https://unitedajodinsurance.com/board-of-directors"}]
            )
            return[]

        elif company_info == "management team":
            dispatcher.utter_message(
                text=f"Click the button below to view our management team.",
                buttons=[
                    {"title": "Management Team",
                     "link": "https://unitedajodinsurance.com/management-team"}]
            )
            return[]

        else:
            try:
                with open('actions/responses/company_profile.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('company_profile')

                    dispatcher.utter_message(json_message=response)
                    return []
            except Exception as error:
                print(error)
            return[]
