import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv());
from actions.actionServices.httpApi import http_post;
from actions.emailService import sendCustomEmail

#environmental varialbles
admin_token = os.getenv('ADMIN_TOKEN')
bot_token=os.getenv('BOT_TOKEN')
organization_id = os.getenv('ORGANIZATION_ID')
base_url=os.getenv('BASE_URL');
protocal=os.getenv('DASHBOARD_PROTOCAL');
dashboard_host=os.getenv('DASHBOARD_HOST') or 'localhost'
email_server=os.getenv('EMAIL_SERVER');
send_Email=os.getenv('SEND_EMAIL')

def DASHBOARD_POST_LEAD(data):
        url = f"{protocal}{dashboard_host}/rest/v1/Organizations/{organization_id}/leads";
        headers = {'content-type': 'application/json', 'Authorization': bot_token };
        http_post(url,headers,data);
        
        
        
def SENDEMAIL(data):
        subject="Customer with following info wants to interect with you:"
        html=f"<div><ul style='list-style:none'><li><b>Descriptions:</b> {data['description']}</li><li><b>Customer/User:</b> {data['fullname']}</li><li><b>Phone No/Email:</b> {data['mobile_email']}</li></ul> </div>"  
        sendCustomEmail(html,subject)