from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import re
from actions.actionServices.leadCaptureService import DASHBOARD_POST_LEAD, SENDEMAIL
from actions.actionServices.feedbackService import DASHBOARD_POST_FEEDBACK, DASHBOARD_POST_COMPLAINTS, SENDEMAIL_FEEDBACK, SENDEMAIL_COMPLAINTS
from actions.actionServices.leadCaptureService import DASHBOARD_POST_LEAD, SENDEMAIL
from actions.actionServices.httpApi import http_get_fb_details
import os
from dotenv import load_dotenv, find_dotenv



# used to load environment variables from a
# ".env" file into your Python environment
load_dotenv(find_dotenv())



class resetFeedbackComplaintsForm(Action):
    def name(self):
        return "action_reset_feedback_complaints_slot"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("feedback_complaints_suggestions", None),
            SlotSet("feedback_complaints_problems", None),
            SlotSet("lead_interest", None)]
        # SlotSet("product_type", None)]


class ValidateFeedbackComplaintsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_feedback_complaints_form"

    def validate_feedback_complaints_full_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        feedback_complaints_full_name = tracker.get_slot(
            "feedback_complaints_full_name")
        is_valid_name = re.match(
            r'^[a-zA-Z]{2,}( {1,2}[a-zA-Z]{2,}){0,}$', feedback_complaints_full_name)
        if len(feedback_complaints_full_name) == 0:
            dispatcher.utter_message(text="Full Name is required.")
            return {"feedback_complaints_full_name": None}
        if is_valid_name is None:
            dispatcher.utter_message(text="Please give valid Name")
            return {"feedback_complaints_full_name": None}
        return {"feedback_complaints_full_name": feedback_complaints_full_name}

    def validate_feedback_complaints_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        mobile_email = tracker.get_slot("feedback_complaints_phone_number")
        is_valid_mobile_email = re.match(r'^(\d{10})$', mobile_email)
        if len(mobile_email) == 0:
            dispatcher.utter_message(text="Phone No is required.")
            return {"feedback_complaints_phone_number": None}
        if(is_valid_mobile_email is None):
            dispatcher.utter_message(text="Invalid contact number.")
            return {"feedback_complaints_phone_number": None}
        return {"feedback_complaints_phone_number": mobile_email}

    def validate_feedback_complaints_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        email = tracker.get_slot("feedback_complaints_email")
        is_valid_email = re.match(
            r'^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$', email)
        if len(email) == 0:
            dispatcher.utter_message(text="Email is required.")
            return {"feedback_complaints_email": None}
        if(is_valid_email is None):
            dispatcher.utter_message(text="Invalid Email.")
            return {"feedback_complaints_email": None}
        return {"feedback_complaints_email": email}

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        additional_slots = []
        feedback_type = tracker.get_slot("feedback_type")

        if(feedback_type == 'feedback'):
            additional_slots.append("feedback_complaints_suggestions")
            return additional_slots + domain_slots

        elif feedback_type == "callback":
            additional_slots.append("lead_interest")
            return additional_slots + domain_slots
        
        elif feedback_type == "buy_policy":
            # additional_slots.append("type_of_product")
            # return additional_slots + domain_slots
            return domain_slots
        
        elif(feedback_type == 'complain' or not feedback_type):
            additional_slots.append("feedback_complaints_problems")
            return additional_slots + domain_slots

        # return domain_slots

    def validate_feedback_complaints_problems(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        feedback_complaints_problems = tracker.get_slot(
            "feedback_complaints_problems")
        return {"feedback_complaints_problems": feedback_complaints_problems}

    def validate_feedback_complaints_suggestions(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        feedback_complaints_suggestions = tracker.get_slot(
            "feedback_complaints_suggestions")
        return {"feedback_complaints_suggestions": feedback_complaints_suggestions}

    def validate_lead_interest(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        lead_interest = tracker.get_slot(
            "lead_interest")
        return {"lead_interest": lead_interest}

    # def validate_type_of_product(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict
    # ) -> Dict[Text, Any]:
    #     type_of_product = tracker.get_slot(
    #         "type_of_product")
    #     return {"type_of_product": type_of_product}

class ActionFeedbackSubmit(Action):
    def name(self) -> Text:
        return "action_feedback_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        # print("form subbmit")
        customerName = tracker.get_slot("feedback_complaints_full_name")
        source = 'Web'
        phonenumber = tracker.get_slot("feedback_complaints_phone_number")
        sender_id = tracker.sender_id

        print("I am inside forms")
        if tracker.slots.get("feedback_type", None) == "feedback":
            source = 'Facebook'
            feedback = {
                'full_name': customerName,
                'mobile_number': tracker.get_slot("feedback_complaints_phone_number"),
                'email_address': tracker.get_slot("feedback_complaints_email"),
                'suggestion': tracker.get_slot("feedback_complaints_suggestions"),
                "organizationId": os.getenv('ORGANIZATION_ID')
            }

            DASHBOARD_POST_FEEDBACK(feedback, sender_id)
            dispatcher.utter_message(response="utter_thankyou_for_feedback",
                                     Name=customerName,
                                     Suggestion=tracker.get_slot(
                                         "feedback_complaints_suggestions"),
                                     Mobile_number=tracker.get_slot(
                                         "feedback_complaints_phone_number"),
                                     )
            SENDEMAIL_FEEDBACK(feedback)
        elif tracker.slots.get("feedback_type", None) == "complain" or tracker.slots.get("feedback_type", None) == None:
            source = 'Facebook'
            complaints = {
                'full_name': customerName,
                'mobile_number': tracker.get_slot("feedback_complaints_phone_number"),
                'email_address': tracker.get_slot("feedback_complaints_email"),
                'title': tracker.get_slot("feedback_complaints_problems"),
                'problem': tracker.get_slot("feedback_complaints_problems"),
                "organizationId": os.getenv('ORGANIZATION_ID')
            }
            DASHBOARD_POST_COMPLAINTS(complaints, sender_id)
            dispatcher.utter_message(response="utter_thankyou_for_complaints",
                                     Name=customerName,
                                     Problems=tracker.get_slot(
                                         "feedback_complaints_problems"),
                                     Mobile_number=tracker.get_slot(
                                         "feedback_complaints_phone_number"),
                                     )
            SENDEMAIL_COMPLAINTS(complaints)

        if tracker.slots.get("feedback_type", None) == "callback":
            source = 'Facebook'
            lead = {
                'fullname': customerName,
                'mobile_email': tracker.get_slot("feedback_complaints_phone_number"),
                'description': "",
                'source': source,
                'visitorId': tracker.sender_id,
                'location': '',
                # 'email_address': tracker.get_slot("feedback_complaints_email"),
                'interest': tracker.get_slot("lead_interest")
                # "organizationId": os.getenv('ORGANIZATION_ID')
            }

            DASHBOARD_POST_LEAD(lead)
            dispatcher.utter_message(response="utter_thankyou_for_info",
                                     Name=customerName,
                                     Interest=tracker.get_slot(
                                         "lead_interest"),
                                     Mobile_number=tracker.get_slot(
                                         "feedback_complaints_phone_number"),
                                     )

        if tracker.slots.get("feedback_type", None) == "buy_policy":         # ---> "feedback_type" is an "entities" and [tracker.slots.get()] &  [tracker.getSlots()] are same
            source = 'Facebook'
            product_type = tracker.get_slot("product_type")
            if product_type is not None:
                abc = f"Purchase {product_type} Plan"
            else:
                abc = f"Insurance Purchase"
            lead = {
                'fullname': customerName,
                'mobile_email': tracker.get_slot("feedback_complaints_phone_number"),
                'description': "",
                'source': source,
                'visitorId': tracker.sender_id,
                'location': '',
                # 'email_address': tracker.get_slot("feedback_complaints_email"),
                'interest': abc
                # "organizationId": os.getenv('ORGANIZATION_ID')
            }

            DASHBOARD_POST_LEAD(lead)
            dispatcher.utter_message(response="utter_thankyou_for_interest",
                                     Name=customerName,
                                     Interest=abc,
                                     Mobile_number=tracker.get_slot(
                                         "feedback_complaints_phone_number"),
                                     )
