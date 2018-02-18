import requests
import json

apiKey = '2536aad057261efff2de419c3f9ec4e1'

def get_loans_from_account(account_id):
    url = 'http://api.reimaginebanking.com/accounts/{}/loans?key={}'.format(account_id,apiKey)
    
    # Retrieve Loans
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        loans = []
        for loan in json_data:
            loans.append(loan)
        return loans
    else:
        return 'Failed to fulfill request with code: ' + str(response.status_code)

