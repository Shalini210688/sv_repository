import getpass

class BankTransaction:
    def __init__(self, acc_balance):
        self.balance = acc_balance

    def deposit(self, amt):
        self.balance += amt
        print("Deposited Rs",amt,"\nThe new balance is ", self.balance)

    def withdraw(self, amt):
        self.balance -= amt
        print("Withdrawn Rs", amt,"\nThe new balance is ", self.balance)

    def bal_check(self):
        print("Your current balance is ", self.balance)


ch = ''
pin = getpass.getpass("Please enter your pin: ")
if pin == '1234':
    obj = BankTransaction(1000)
    while ch != '0':
        print("""
                 Enter   1 for Withdrawal
                            2 for Deposit
                            3 for balance check
                            0 to exit""")
        ch = input(">")
        if ch == '1':
            amount = int(input("Enter amount to withdraw: "))
            obj.withdraw(amount)
        elif ch == '2':
            amount = int(input("Enter amount to deposit: "))
            obj.deposit(amount)
        elif ch == '3':
            obj.bal_check()
        else:
            break




