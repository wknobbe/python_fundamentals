class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def display_info(self):
        info_dict = {'Name': self.name, 'Email Address': self.email, 'Account Balance': self.balance}
        print(info_dict)
    def deposit(self,amount):
        self.balance += amount
        print(f"A deposit of {amount} was made to your account")
    def withdrawal(self,amount):
        self.balance -= amount
        print(f"A withdrawl of {amount} was made from your account")
    def transfer(self,user,amount):
        user.balance -= amount
        self.balance += amount
        print(f"There has been a transfer of {amount} from {user.name} to your account")

bob = User("Bob", "bob@python.net")
sara = User("Sara", "sara@python.net")
bob.display_info()
sara.display_info()
bob.deposit(250)
sara.transfer(bob,100)
bob.display_info()
sara.display_info()