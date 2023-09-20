from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionOfficeTimes(Action):

    def name(self) -> Text:
        return "action_office_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text=f"Our Opening hours are Sunday to Friday 9:30 am to 5:30 pm."
        )
        return[]
