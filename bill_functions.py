import requests
import json

apiKey = '2536aad057261efff2de419c3f9ec4e1'

def get_bills_from_customer(customer_id):
    url = 'http://api.reimaginebanking.com/customers/{}/bills?key={}'.format(customer_id,apiKey)
    
    # Retrieve Bills
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        bills = []
        for bill in json_data:
            bills.append(bill)
        return bills
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)

def get_bills_from_account(account_id):
    url = 'http://api.reimaginebanking.com/accounts/{}/bills?key={}'.format(account_id,apiKey)
    
    # Retrieve Bills
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        bills = []
        for bill in json_data:
            bills.append(bill)
        return bills
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)
