from customer_functions import customer_from_name
from account_functions import retrieve_accounts, retrieve_transfers
from bill_functions import get_bills_from_customer
from loan_functions import get_loans_from_account
from withdrawal_functions import get_withdrawals_from_account
from deposit_functions import get_deposits_from_account
import pygal
from pygal.style import LightGreenStyle
from flask import Flask, render_template
app = Flask(__name__)

customer_id = '' 

@app.route('/')
def index():
    # This would be dynamically retrieved
    first_name = 'Brendan'
    last_name = 'Sherman'
    full_name = first_name + ' ' + last_name
    customer = customer_from_name(full_name)
    loan_total = 0
    bill_total = 0
    withdrawal_total = 0
    transfer_list = []
    deposit_list = []
    
    # Insert Error Handling Here
    
    # Get customer information
    global customer_id
    customer_id = customer['_id']
    address = customer['address']
    address1 = address['street_number'] + ' ' + address['street_name']
    address2 = address['city'] + ', ' + address['state'] + ' ' + address['zip']
    
    # Get accounts
    accounts = retrieve_accounts(customer_id)
    
    # Get pending transfers
    pending_transfers = []
    for account in accounts:
        transfers = retrieve_transfers(account['_id'], 'payer')
        for transfer in transfers:
            pending_transfers.append(transfer)
        transfers = retrieve_transfers(account['_id'], 'payee')
        for transfer in transfers:
            transfer_list.append(transfer['amount'])
    num_pending = len(pending_transfers)
    
    # Get bills
    bills = get_bills_from_customer(customer_id)
    for bill in bills:
        bill_total+=bill['payment_amount']
    
    # Get Loans
    all_loans = []
    for account in accounts:
        loans = get_loans_from_account(account['_id'])
        for loan in loans:
            all_loans.append(loan)
            loan_total+=loan['amount']
    
    # Get Withdrawals
    all_withdrawals = []
    for account in accounts:
        withdrawals = get_withdrawals_from_account(account['_id'])
        for withdrawal in withdrawals:
            all_withdrawals.append(withdrawal)
            withdrawal_total+=withdrawal['amount']
    
    # Get Deposits
    for account in accounts:
        deposits = get_deposits_from_account(account['_id'])
        for deposit in deposits:
            deposit_list.append(deposit['amount'])
    
    # Create account pie chart
    pie_chart = pygal.Pie(legend_font_size=54, title_font_size=72, style=LightGreenStyle, disable_xml_declaration=True)
    pie_chart.title = 'Account Balances'
    for account in accounts:
        pie_chart.add(account['nickname'], account['balance'])
    
    # Create spending bar graph
    bar_graph = pygal.HorizontalBar(legend_font_size=54, title_font_size=72, style=LightGreenStyle, disable_xml_declaration=True)
    bar_graph.title = 'Money to be Used for Services'
    bar_graph.add('Loans', loan_total)
    bar_graph.add('Bills', bill_total)
    bar_graph.add('Withdrawals', withdrawal_total)
    
    # Create revenue dot plot
    dot_plot = pygal.Dot(x_label_rotation=30, legend_font_size=54, title_font_size=72, style=LightGreenStyle, disable_xml_declaration=True)
    dot_plot.title = 'Revenue'
    dot_plot.add('deposits', deposit_list)
    dot_plot.add('transfers', transfer_list)
    
    return render_template('index.html', customer_id=customer_id, name=full_name, address1=address1, address2=address2, accounts = accounts, pending_transfers=transfers, num_pending=num_pending, bills=bills, pie_chart=pie_chart, all_withdrawals=all_withdrawals, bar_graph=bar_graph, dot_plot=dot_plot)

if __name__ == "__main__":
    app.run()
