from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action, Tracker, FormValidationAction


class ActionSayData(Action):
    def name(self) -> Text:
        return "action_say_data"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            name= tracker.get_slot("name")
            city= tracker.get_slot("city")
            phone= tracker.get_slot("phone")


            dispatcher.utter_message(text= f"Hey {name}, {city} is a very beautiful place.Your phone number is {phone} : )")

            return []
            
            
class ValidateSimpleForm(FormValidationAction):
     def name(self) -> Text:
          return "validate_simple_form"
     
     def validate_phone(self, slot_value: Any, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          
          phone= tracker.get_slot("phone")

          if(int(len(phone))>10):
               dispatcher.utter_message(text= "Invalid phone number")
               return{"phone": None}
          
          if(int(len(phone))<10):
               dispatcher.utter_message(text= "Invalid phone number")
               return {"phone": None}
          else:
               return {"phone": phone}
          

     def validate_name(self, slot_value: Any, dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = slot_value.strip()

        # Check if the name contains any digits
        if any(c.isdigit() for c in name):
            dispatcher.utter_message(text="Invalid name: Names should not contain numbers.")
            return {"name": None}
        else:
            return {"name": name}     
                 

     def validate_city(self, slot_value: Any, dispatcher: CollectingDispatcher,
                         tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          city = slot_value.strip()

          # Check if the city contains any digits
          if any(c.isdigit() for c in city):
               dispatcher.utter_message(text="Invalid city: City names should not contain numbers.")
               return {"city": None}
          else:
               return {"city": city}                

  

     def validate_ask_partial_data_confirmation(
               self,
               slot_value: Any,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
          ) -> List[Dict[Text, Any]]:
          if slot_value.lower() == "yes":
               dispatcher.utter_message(text="Submitting the form with the provided information.")
               return {"ask_partial_data_confirmation": slot_value}
          else:
               # If the user doesn't want to fill this field, skip the corresponding slot
               slot_to_skip = tracker.get_slot("requested_slot")
               if slot_to_skip == "city":
                    dispatcher.utter_message(text="Skipping the city slot.")
                    return {"ask_partial_data_confirmation": slot_value, "city": None}
               else:
                    dispatcher.utter_message(text="Resuming form filling.")
                    return {"ask_partial_data_confirmation": None}