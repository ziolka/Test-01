class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount} units"
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount} units"
        else:
            return "Invalid amount or insufficient balance"

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.deposit(500))  # Deposited 500 units
print(account.withdraw(200))  # Withdrew 200 units
print(account.get_balance())  # 1300