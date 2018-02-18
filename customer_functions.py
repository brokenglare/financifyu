import requests
import json

apiKey = '2536aad057261efff2de419c3f9ec4e1'
url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

def customer_from_name(full_name):
    # Retrieve Customers
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        
        for customer in json_data:
            customer_name = customer['first_name'] + ' ' + customer['last_name']
            if customer_name == full_name:
                return customer
        return 'Failed to find id for: ' + full_name
    else:
        return 'Failed to fulfill request with code: ' + response.status_code
