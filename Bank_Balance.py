# Python program to create Bankaccount class
class Bank_Account:

    def __init__(self):
        self.balance = 1000
        print ('Hello, Welcome to the Deposit & Withdrawal Machine')

    def withdraw(self):
        amount = float(input('Enter amount to be withdrawn: '))
        if self.balance >= amount:
            self.balance -= amount
            if self.balance <= 1000:
                self.balance += amount
                print ('If account balance is less than Rs.1000, then you can not withdraw amount.')
                
            else:
                print ('\n You Withdrew:', amount)
        else:
            print ('\n Insufficient balance!!! ')

    def display(self):
        print ('\n Net Available Balance=', self.balance)


s = Bank_Account()

s.withdraw()
s.display()