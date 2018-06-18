#worldcup2018-notifier - Python Lambda Function for send email when a game is available
#You need to add permission to run SES in the IAM role for this function
#Apart from that create an event in CloudWatch to trigger this function every minute to verify availability
#Change the email_from = 'xxxx', email_to = 'xxxxx' in the code and verify them in the SES
#The default daily limit of SES is 200 emails/day. So you have to ask AWS to increase this quota.

from __future__ import print_function
from botocore.vendored import requests
import json
import boto3

ses = boto3.client('ses')

email_from = 'xxxx'
email_to = 'xxxxx'
email_subject = 'There is tickets available!!'
email_body = 'Body'


threshold = 0
categories = ["CAT 1","CAT 2","CAT 3" ]
productId = ["IMT11", "IMT15"]
games = {"IMT11": "Match 11 - Germany v Mexico - Moscow Luzhniki", "IMT15": "Match 15 - Senegal v Polland - Moscow Luzhniki"}

def lambda_handler(event, context):
    response = "No tickets available"
    tix_data = requests.get("https://tickets.fifa.com/API/WCachedL1/en/BasicCodes/GetBasicCodes?currencyId=USD")
    tix = tix_data.text
    tx = json.loads(tix)
    tickets = checkAvailability (tx);
    if (len(tickets) > 0):
        response = "There is tickets available!!"
        sendEmail(tickets)
    return response

def checkAvailability(data):
    ticketsAvailable = []
    pricesArray = data["Data"]["PRODUCTPRICES"]
    for product in pricesArray:
        if (product["PRPProductId"] in productId and product["CategoryName"] in categories and product["Availability"] > threshold):
            print("ProductId: " + product["PRPProductId"])
            print("CategoryName: " + product["CategoryName"])
            print("Availability: ", product["Availability"])
            ticketsAvailable.append(product)
    return ticketsAvailable 

def sendEmail(tickets):
    email_body = ""
    email_subject = 'Tickets available' 
    productBefore = ""
    for ticket in tickets:
        if(productBefore != ticket["PRPProductId"]):
            email_subject += ", " + str(ticket["PRPProductId"])
            productBefore = ticket["PRPProductId"]
            email_body += str(games[ticket["PRPProductId"]]) + "\n"
        email_body += str(ticket["PRPProductId"]) + " " + str(ticket["CategoryName"]) + " - Total: " + str(ticket["Availability"]) + "\n "
        response = ses.send_email(
            Source = email_from,
            Destination={
                'ToAddresses': [
                    email_to,
                ]
            },
            Message={
                'Subject': {
                    'Data': email_subject
                },
                'Body': {
                    'Text': {
                        'Data': email_body
                    }
                }
            }
        )

    






