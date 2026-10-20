balance = 3000

def show():
    global balance
    deposit = 1000
    balance = balance + deposit
    print("Deposit Balance:", deposit)

    print("Initial Balance was:", global() ["balance"])

show()
print("Current Balance After Deposit:", balance)