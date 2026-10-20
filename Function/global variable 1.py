balance=3000 # Global Variable

def show():

    global balance
    deposit=1000
    print("Deposit Balance: ", deposit)

    balance balance+deposit

show()
print("Current Balance After Deposit: ", balance)