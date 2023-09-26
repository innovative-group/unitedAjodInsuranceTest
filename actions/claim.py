from typing import Any, Dict, List, Optional, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from rasa_sdk.events import SlotSet, AllSlotsReset



class AboutClaim(Action):
    def name(self) -> Text:
        return "action_about_claim"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:



        
        dispatcher.utter_message(
            text=f"Please click the button below for different claim related services.",
            buttons=[
                {"title": "Claim Procedure",
                 "payload": f"/procedure{{\"insurance_info\":\"claim\"}}"},
                {"title": "File a Claim",
                 "payload": f"/file_a_claim"},
                {"title": "Check Claim Status",
                 "payload": f"/claim_status"},
                {"title": "Required Documents for Claim",
                 "payload": f"/document_required{{\"claim_doc\":\"claim\"}}"}
            ]
        )
        return[]


class FileAClaim(Action):
    def name(self) -> Text:
        return "action_file_a_claim"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        method = tracker.get_slot("method")
        claimType= tracker.get_slot("claimType")

        print(" \n\n -----> value of [method]= ", method)
        print("  -----> value of [claimType]=  ", claimType, "\n\n")

        if method == "online":
            if claimType == "motor insurance claim":
                print("\n\n ----->> inside [online][motorClaim] <<-------\n\n")
                try:
                    with open('actions/responses/claim.json', 'r', encoding='utf-8') as f:
                        print("Testing")
                        data = json.load(f)
                        response = data.get('motorClaim')
                        dispatcher.utter_message(json_message=response)
                except Exception as error:
                    print(error)
                                    
                return[]
            
            elif claimType == "non motor insurance claim":
                print("\n\n ----->> [online][nonMotorClaim] <<-------\n\n")
                try:
                    with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                        data = json.load(f)
                        response = data.get('non_motorClaim')
                        dispatcher.utter_message(json_message=response)
                except Exception as error:
                    print(error)
                return[]                

            else:
                print("\n\n ---> inside [online][else] <<-----\n\n")
                buttons = [

                {"title": "Motor Insurance Claim",
                    "payload": f"/file_a_claim{{\"claimType\":\"motor insurance claim\", \"method\": \"online\"}}"},
                
                {"title": "Non Motor Insurance Claim",
                    "payload": f"/file_a_claim{{\"claimType\":\"non motor insurance claim\", \"method\": \"online\"}}"},                     
                
            ]

            dispatcher.utter_message(
                text=f"Pleeas choos the option below to report a claim.",
                buttons=buttons
            )

        
        elif method == "contact":
            print("\n\n ----->> inside contact <<-------\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('headOffice')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]    
        
        else:

            print("\n\n----->> else block <<-------\n\n")
            buttons = [

                {"title": "File online claim",
                    "payload": f"/file_a_claim{{\"method\":\"online\"}}"},
                
                {"title": "Our HeadOffice",
                    "payload": f"/file_a_claim{{\"method\":\"contact\"}}"},                     
                
            ]

            dispatcher.utter_message(
                text=f"Please fill up the given form to register your claim.",
                buttons=buttons
            )
            
            return[]


class ClaimStatus(Action):
    def name(self) -> Text:
        return "action_claim_status"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        insurance_info = tracker.get_slot("insurance_info")
        method = tracker.get_slot("method")

        if method == "online claim":
            try:
                with open('actions/responses/claim.json', 'r') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('claim_status')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)

            return[]

        else:
            dispatcher.utter_message(
                text=f"Please fill up the given form to track your claim online.",
                buttons=[
                    {
                        "title": "Track your Claim",
                        "payload": f"/claim_status{{\"document\":\"form\"}}"
                    }
                ]
            )
            return[]


class ClaimStatus(Action):
    def name(self) -> Text:
        return "action_document_required"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        claim_doc = tracker.get_slot("claim_doc")
        print("\n\n ------------->> ", claim_doc , "<<------------\n\n")
        if claim_doc == "engineering claim":
            print("\n\n---->> inside engineering claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    print("Testing")
                    data = json.load(f)
                    response = data.get('er_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)

            return[]
        
        elif claim_doc == "fire claim":
            print("\n\n---->> inside fire claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('fire_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        
        elif claim_doc == "theft claim":
            print("\n\n---->> inside vehicle theft claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('theft_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]    

        elif claim_doc == "marine insurance claim":
            print("\n\n---->> inside marine claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('marine_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        
        elif claim_doc == "accident claim":
            print("\n\n---->> inside accident claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('pa_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]    

        

        elif claim_doc == "micro insurance claim":
            print("\n\n---->> micro insurance claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('micro_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        
        elif claim_doc == "third party claim":
            print("\n\n---->> third party claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('third_party_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]    
        

        
        elif claim_doc == "motor policy claim":
            print("\n\n---->> motor policy claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('motor_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]
        
        elif claim_doc == "human death claim":
            print("\n\n---->> human death claim <<----\n\n")
            try:
                with open('actions/responses/claim.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                    response = data.get('passenger_docForClaim')
                    dispatcher.utter_message(json_message=response)
            except Exception as error:
                print(error)
            return[]    
        
        




        else:
            print(" \n\n *************| outer else block | ****************\n\n")
            return[]
        

    