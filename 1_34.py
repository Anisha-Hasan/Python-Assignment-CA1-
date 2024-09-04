
def compute_net_amount(transactions):
    net_amount = 0
    for transaction in transactions:

        type, amount = transaction.split()
        amount = int(amount)  
        
        if type == 'D':
            net_amount += amount
        elif type == 'W':
            net_amount -= amount
        else:
            print("Invalid transaction type:", type)
    
    return net_amount


def input_transactions():
    transactions = []
    print("Enter transaction log (type '!' to finish):")
    while True:
        line = input()
        if line == '!':
            break
        transactions.append(line)
    return transactions

transactions = input_transactions()

net_amount = compute_net_amount(transactions)

print("Net amount:", net_amount)
