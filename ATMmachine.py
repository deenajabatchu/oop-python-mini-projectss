class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None


atm = ATM()
acc1 = Account("1234", "0000", 5000)
atm.add_account(acc1)

user = atm.authenticate("1234", "0000")
if user:
    user.check_balance()
    user.deposit(1000)
    user.withdraw(2000)
else:
    print("Authentication Failed")
