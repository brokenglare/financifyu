import requests
import json

apiKey = '2536aad057261efff2de419c3f9ec4e1'

def get_withdrawals_from_account(account_id):
    url = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(account_id,apiKey)
    
    # Retrieve Withdrawals
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        withdrawals = []
        for withdrawal in json_data:
            withdrawals.append(withdrawal)
        return withdrawals
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)
