import requests
import json

apiKey = '2536aad057261efff2de419c3f9ec4e1'

def get_deposits_from_account(account_id):
    url = 'http://api.reimaginebanking.com/accounts/{}/deposits?key={}'.format(account_id,apiKey)
    
    # Retrieve Deposits
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        deposits = []
        for deposit in json_data:
            deposits.append(deposit)
        return deposits
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)
