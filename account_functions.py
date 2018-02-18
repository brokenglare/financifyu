import requests
import json
import datetime

apiKey = '2536aad057261efff2de419c3f9ec4e1'

def retrieve_accounts(customer_id):
    # Set url
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id, apiKey)
    # Retrieve Accounts of Customer
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        return json_data
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)

def retrieve_transfers(account_id, pay_type):
    url = 'http://api.reimaginebanking.com/accounts/{}/transfers?type={}&key={}'.format(account_id, pay_type, apiKey)
    # Retrieve Transferds of Customer
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        transfers = []
        for transfer in json_data:
            transfers.append(transfer)
        return transfers
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)

def create_transfer(payer_account_id, payee_account_id, medium, amount, description):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    date_string = str(year) + '-' + str(month) + '-' + str(day)
    
    url = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(payer_account_id, apiKey)
    payload = {
        "medium": medium,
        "payee_id": payee_account_id,
        "amount": amount,
        "transaction_date": date_string,
        "status": 'pending',
        "description": description,
    }
    
    # Create a Transfer
    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
        )

    if response.status_code == 201:
        print('tranfer created')
    else:
        print(response.status_code)
