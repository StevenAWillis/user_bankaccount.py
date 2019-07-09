class BankAccount:

    def __init__(self,int_rate,account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance += amount
        return self
        
    def widthdrawal(self,amount):
        if(self.account_balance < amount):
            print("Insuficient Funds")
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f" Balance: ${self.account_balance}")
        return self

    def yield_int(self):
        if(self.account_balance >0):
            interest = self.account_balance * self.int_rate
            BPlusInt = self.account_balance + interest
            print(f"Yield Interest: ${interest}, Balance W/Int: ${BPlusInt}")
        return self    



class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02,account_balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self	
    
    def make_widthdrawal(self, amount):
        self.account.widthdrawal(amount)	
        return self
    def display_user_balance(self):
        print(f" User: {self.name}  , Balance: ${self.account.account_balance} ")
        return self
    def transfer_money(self,other_user,amount):
        self.account.widthdrawal(amount)
        other_user.account.deposit(amount)    
        return self

guido = User("Guido van Rossum", "guido@python.com")  
emmy = User("Emmy Tan", "emmy@python.com")
steebo = User("Steebo Steak", "stebo@python.com")

steebo.display_user_balance()
steebo.make_deposit(1000)
steebo.display_user_balance()
steebo.make_widthdrawal(10)
steebo.display_user_balance()

guido.display_user_balance()
guido.make_deposit(1000)
guido.display_user_balance()
guido.make_widthdrawal(10)
guido.display_user_balance()

steebo.display_user_balance()
guido.display_user_balance()
steebo.transfer_money(guido,40)
guido.display_user_balance()
steebo.display_user_balance()

# user001 = BankAccount(0.007, 500)
# user002 = BankAccount(0.006, 600)
# user003 = BankAccount(0.006, 600)

# user001.deposit(100).deposit(100).deposit(100).widthdrawal(50).display_account_info().yield_int()

# user002.deposit(1000).widthdrawal(100).widthdrawal(100).widthdrawal(50).widthdrawal(150).display_account_info().yield_int()