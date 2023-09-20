from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import AllSlotsReset


class ActionCancelSubscription(Action):

    def name(self) -> Text:
        return "action_cancel_subscription"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(
            text=f"The insurance may be terminated at any time at the request of the insured, in which case the company will retain the premium calculated at the customary short period rate for the time the policy has been in force.")

        dispatcher.utter_message(
            text="This insurance may also get terminated at any time with respect to the option of the company with 7 days prior notice to the insured.")

        dispatcher.utter_message(text="For example, In case of request made by insured to cancel the Everest Travel Trip Insurance with valid reason within Policy period a refund premium of 75 percent on total premium will be allowed to Insured. For more information please contact to our branch.",
                                 buttons=[{
                                     "title": "Branch",
                                     "payload": f"branch office"
                                 }]
                                 )
        return []
