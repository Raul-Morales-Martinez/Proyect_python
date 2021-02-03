
class BankAccount:
    def __init__(self, ncuenta, int_rate,  balance=0): # don't forget to add some default values for these parameters!
        self.in_rate = int_rate
        self.balance = balance
        self.ncuenta = ncuenta

    # def deposit(self, amount):
    #     self.balance += amount
    #     return self
    # def withdraw(self, amount):
    #     self.balance -= amount
    #     return self
    # def display_account_info(self):
    #     print("El monto en la cuenta es de: $",self.balance)
    # def yield_interest(self):
    #     interes = self.balance * self.in_rate
    #     print("El interes es de: $",interes)
    #     return self

# n1010 = BankAccount (0.02,200)
# n1011 = BankAccount (0.01)

# n1010.deposit(100).deposit(150).deposit(150).withdraw(10).yield_interest().display_account_info()
# n1011.deposit(1500).deposit(800).withdraw(150).withdraw(20).withdraw(100).withdraw(5).yield_interest().display_account_info()


class User:
    def __init__(self, name, email, ncuenta):
        self.name = name
        self.email = email
        self.account = BankAccount(ncuenta, int_rate=0.02,  balance=0)# added this line

    def deposit(self, amount):
        self.account.balance += amount
        return self

    def withdraw(self, amount):
        self.account.balance -= amount
        return self

    def display_account_info(self):
        print("El monto en la cuenta es de: $", self.account.balance)

    def yield_interest(self):
        interes = self.account.balance * self.account.in_rate
        print("El interes es de: $", interes)
        return self

    def example_method(self):
        self.account.deposit(100)  # we can call the BankAccount instance's methods
        print(self.account.balance)  # or access its attributes

monty = User("Monty Python", "monty@python.com", "n0001")
monty.display_account_info()
monty.deposit(10)
monty.display_account_info()