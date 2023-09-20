from actions.actionServices.httpApi import http_post
from actions.emailService import sendCustomEmail
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# environmental varialbles
admin_token = os.getenv('ADMIN_TOKEN')
bot_token = os.getenv('BOT_TOKEN')
organization_id = os.getenv('ORGANIZATION_ID')
base_url = os.getenv('BASE_URL')
protocal = os.getenv('DASHBOARD_PROTOCAL')
dashboard_host = os.getenv('DASHBOARD_HOST') or 'localhost'
email_server = os.getenv('EMAIL_SERVER')
send_Email = os.getenv('SEND_EMAIL')


def DASHBOARD_POST_FEEDBACK(data, sender_id):
    url = f"{protocal}{dashboard_host}/rest/v1/visitors/{sender_id}/feedbacks/create"
    headers = {'content-type': 'application/json',
               'Authorization': admin_token}
    data = http_post(url, headers, data)
    print(data, "=========response========")


def DASHBOARD_POST_COMPLAINTS(data, sender_id):
    url = f"{protocal}{dashboard_host}/rest/v1/visitors/{sender_id}/complaints/create"
    headers = {'content-type': 'application/json',
               'Authorization': admin_token}
    http_post(url, headers, data)


def SENDEMAIL_COMPLAINTS(data):
    subject = "Complaints filed by user:"
    html = f"<div><ul style='list-style:none'><b>Customer/User:</b> {data['full_name']}</li><li><b>Phone No:</b> {data['mobile_number']}</li></li><li><b>Email:</b> {data['email_address']}</li><li><b>Problem:</b> {data['problem']}</li><li></ul> </div>"
    sendCustomEmail(html, subject)


def SENDEMAIL_FEEDBACK(data):
    subject = "Suggestions provided by user:"
    html = f"<div><ul style='list-style:none'><b>Customer/User:</b> {data['full_name']}</li><li><b>Phone No:</b> {data['mobile_number']}</li></li><li><b>Email:</b> {data['email_address']}</li><li><b>Suggestions:</b> {data['suggestion']}</li><li></ul> </div>"
    sendCustomEmail(html, subject)
