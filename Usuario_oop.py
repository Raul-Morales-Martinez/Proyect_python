
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal (self, cantidad):
        self.account_balance -= cantidad
        return self
    def display_user_balance (self):
        print("Usuario:",self.name,",","saldo: $",self.account_balance)
        return self
    def transfer_money (self, other_user, cantidadd) :
        self.account_balance -= cantidadd
        other_user.make_deposit(cantidadd)
        return self

guido = User ("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(150)
guido.make_withdrawal(50)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(100)
monty.make_withdrawal(10)
monty.make_withdrawal(15)
monty.display_user_balance()

jose = User("Jose de las mercedez","josecito@python.com")
jose.make_deposit(1000)
jose.make_withdrawal(100)
jose.make_withdrawal(150)
jose.make_withdrawal(200)
jose.display_user_balance()

jose.transfer_money(monty,200)
jose.display_user_balance()
monty.display_user_balance()
##
#metodos
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
