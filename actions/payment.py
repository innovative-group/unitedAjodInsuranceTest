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

        khalti_btn = {"title": "Khalti",
                      "link": "https://khalti.com/"
                      }
        esewa_btn = {
            "title": "eSewa",
            "link": "https://esewa.com.np/"
        }
        connectips_btn = {"title": "Connect IPS",
                          "link": "https://www.connectips.com/"}

        imepay_btn = {"title": "IME Pay",
                      "link": "https://www.imepay.com.np/#/"}

        prabhupay_btn = {"title": "Prabhu Pay",
                         "link": "https://prabhupay.com/"}

        if wallet_name == "khalti":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from khalti.",
                buttons=[khalti_btn]
            )
            return[]

        elif wallet_name == "esewa":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from eSewa.",
                buttons=[esewa_btn]
            )
            return[]

        elif wallet_name == "connectips":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from Connect IPS.",
                buttons=[connectips_btn]
            )
            return[]

        elif wallet_name == "ime pay":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from IME Pay.",
                buttons=[imepay_btn]
            )
            return[]

        elif wallet_name == "prabhu pay":
            dispatcher.utter_message(
                text=f"Please click the button below to make payment from Prabhu Pay.",
                buttons=[prabhupay_btn]
            )
            return[]

        else:
            dispatcher.utter_message(
                text=f"We accept the payment from following digital wallets.",
                buttons=[esewa_btn, khalti_btn,
                         connectips_btn, imepay_btn, prabhupay_btn])
            return[]
