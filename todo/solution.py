import random


class Account:

    def __init__(self, balance, account_type, acct_num=random.randrange(10**15, 10**15+1), interest_rate=0.01):
        self.acct_num = acct_num
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = float(interest_rate)

    def set_up(self):
        self.acct_num = random.randrange(10**15, (10**15 +1))
        self.balance = int(input("How much?: "))
        self.account_type = float(input("What type of account?:  "))
        self.interest_rate = input("Current rate is: ")

    @classmethod
    def from_csv_string(Account, account_string):
        new_acct = account_string.split(',')
        account_num, balance, account_type = new_acct
        account = Account(acct_num=account_num, balance=balance, account_type=account_type)

        return account

    def get_funds(self):
        print(self.balance)
        return self.balance

    def deposit(self, amount):
        #deposit = int(input("How much would you like to deposit? "))
        self.balance += amount
        return self.balance

    def check_withdraw(self, withdraw):
        if withdraw > self.balance:
            return False
        else:
            return True

    def withdraw(self, withdrawl_amount):
        new_amount = self.balance - withdrawl_amount

        if new_amount < 0:
            raise ValueError("Insufficient Funds")
        else:
            self.balance = new_amount
            return new_amount

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        return self.balance + interest

    def get_standing(self):
        if self == self:
            return True
