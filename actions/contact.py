from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json




class ActionContact(Action):

    def name(self) -> Text:
        return "action_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        office_type = tracker.get_slot("office_type")
        social_media = tracker.get_slot("social_media")
        user_type = tracker.get_slot("user_type")

        if office_type == "main office":
            try:
                with open('actions/responses/contact.json', 'r') as f:
                    data = json.load(f)
                    response = data.get("headOffice")
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif office_type == "branch office":
            try:
                with open('actions/responses/contact.json', 'r') as f:
                    data = json.load(f)
                    response = data.get("branch_office")
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif office_type == "branch list":
            try:
                with open('actions/responses/contact.json', 'r') as f:
                    data = json.load(f)
                    response = data.get("branch_list")
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        elif office_type == "customer support":
            try:
                with open('actions/responses/contact.json', 'r') as f:
                    data = json.load(f)
                    response = data.get("head_office")
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]

        facebook_button = {"title": "Facebook",
                           "link": "https://www.facebook.com/unitedajodinsurancelimited/"
                           }

        youtube_button = {"title": "YouTube",
                          "link": "https://www.youtube.com/watch?v=E3WjK2FFAbQ"
                          }

        if social_media:
            if social_media == "facebook":
                dispatcher.utter_message(
                    text="Please click the button below to visit the official Facebook page of Siddhartha Insurance and stay connected with us.",
                    buttons=[facebook_button]
                )
                return[]



            elif social_media == "youtube":
                dispatcher.utter_message(
                    text="Please click the button below to visit the official Facebook page of Siddhartha Insurance and stay connected with us.",
                    buttons=[youtube_button]
                )
                return[]

            else:
                dispatcher.utter_message(text=f"Here is the list of our social media handles:",
                                         buttons=[facebook_button, youtube_button])
                return[]

        if user_type == "agent":
            dispatcher.utter_message(
                text=f"To obtain the contact details of insurance agents, please click the button below.",
                buttons=[
                    {
                        "title": "Insurance Agents",
                        "link": f"https://unitedajodinsurance.com/agents"
                    }])
            return[]

        else:
            buttons = [
                {
                    "title": "Head Office",
                    "payload": f"/contact{{\"office_type\":\"main office\"}}"
                },
                {
                    "title": "Nearby Branches",
                    "payload": f"/contact{{\"office_type\":\"branch office\"}}"
                },
                {
                    "title": "Branch List",
                    "payload": f"/contact{{\"office_type\":\"branch list\"}}"
                }
            ]
            dispatcher.utter_message(
                text=f"Please click the buttons below to get the contact details and branch details.",
                buttons=buttons
            )
        return[]
