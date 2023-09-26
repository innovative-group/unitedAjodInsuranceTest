from typing import Any, Dict, List, Optional, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import SlotSet, AllSlotsReset



class Payment(Action):
    def name(self) -> Text:
        return "action_payment"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        payment_option = tracker.get_slot("payment_option")
        wallet_name = tracker.get_slot("wallet_name")

        khalti = {"title": "Khalti",
                      "link": "https://khalti.com/"
                      }
        Esewa = {
            "title": "eSewa",
            "link": "https://esewa.com.np/"
        }
        ConnectIPS = {"title": "Connect IPS",
                          "link": "https://www.connectips.com/"}

        IME_PAY = {"title": "IME Pay",
                      "link": "https://www.imepay.com.np/#/"}

   

        if wallet_name == "khalti":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from khalti.",
                buttons=[khalti]
            )
            return[]

        elif wallet_name == "esewa":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from eSewa.",
                buttons=[Esewa]
            )
            return[]

        elif wallet_name == "connectips":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from Connect IPS.",
                buttons=[ConnectIPS]
            )
            return[]

        elif wallet_name == "ime pay":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from IME Pay.",
                buttons=[IME_PAY]
            )
            return[]

       

        else:
            dispatcher.utter_message(
                text=f"We accept the payment from following digital wallets.",
                buttons=[khalti, Esewa,
                         ConnectIPS, IME_PAY])
            return[]
