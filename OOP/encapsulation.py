#encupsulation = hide details
#access modifiers: private, public,protected
#normal vabe kuno attribute declare korle ta public hobe
#__ dile ta private hobe
#_ dile ta protected hisabe dhore neya hoy

class Bank :
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance=self.__balance-amount
            return amount
rafsan = Bank('choto bhai',10000)
print(rafsan.holder_name)
print(rafsan.get_balance())
