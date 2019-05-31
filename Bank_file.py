import random


class User:

    def __init__(self):
        self.name = ''
        self.age = 0
        self.acc_no = 0
        self.balance = 0

    def set_name(self):
        self.name = raw_input('Name : ')

    def set_age(self):
        self.age = int(input('Age : '))

    def set_acc_no(self):
        self.acc_no = random.randint(1000, 9999)

    def get_name(self):
        return self.name

    def get_accno(self):
        return self.acc_no

    def get_age(self):
        return self.age

    def deposit(self):
        amount = int(input('Enter the amount to be deposited: '))
        if amount <= 0:
            print('Please deposit the valid amount')
        else:
            self.balance += amount

    def withdraw(self):
        try:
            amount = int(input('Enter the amount to be withdrawn: '))
            if amount <= 0:
                raise ValueError('Please Enter the valid Amount')

            elif self.balance < amount:
                raise ValueError('Insufficient Balance')

        except ValueError as e:
            print (e)

        else:
            self.balance -= amount
            return self.balance

    def set_initialbalance(self):
        self.balance = 0
        return self.balance

    def get_balance(self):
        return self.balance


user_list = []

dummy_var = True
while True:

    print '\n\t MAIN MENU\n'
    print '\t1. Account Creation'
    print '\t2. Deposit'
    print '\t3. Withdraw'
    print '\t4. Balance Check'
    print '\t5. Close Account'
    print '\t6. Exit\n'

    ch = input('Choose the services ')

    if ch == 1:
        user = User()
        print '\t \n Account Creation'

        user.set_acc_no()
        user.set_name()
        user.set_age()

        print '\t\t Account Created\n'
        print 'The Account Number is : ', user.acc_no
        print 'Account Holder Name : ', user.get_name()
        print 'Balance : ', user.set_initialbalance()

        user_list.append(user)

    elif ch == 2:

        print '\t Deposit'

        number = int(input('Enter the Account Number '))

        for user in user_list:
            if user.get_accno() == number:
                user.deposit()
                print('\n\t Amount Deposited\n')
                print 'Account Number : ', user.get_accno()
                print 'Account Holder Name: ', user.get_name()
                print 'Account Balance : ', user.get_balance()
                break

        else:
            print('*** Account not existed ***')

    elif ch == 3:

        print '\t Withdrawn\n'
        number = int(input('Enter the Account Number '))
        for user in user_list:
            if user.get_accno() == number:
                user.withdraw()
                break
        else:
            print '*** Account does not exist ***'

    elif ch == 4:

        print '\t Check Balance'
        number = int(input('Enter the Account Number '))
        for user in user_list:
            if user.get_accno() == number:
                print '\n\n\t\t Account Number : ', user.get_accno()
                print '\t\tAccount Holder Name: ', user.get_name()
                print '\t\tAccount Balance : ', user.get_balance()
                break
        else:
            print '*** Account does not exist ***'

    elif ch == 5:

        print '\t Closing Account'
        number = int(input('Enter the Account Number '))
        for user in user_list:
            if user.get_accno() == number:
                print'\n\n\t\t Account has been Closed'
                print '\n\n\t\t Account Number : ', user.get_accno()
                print '\t\tAccount Holder Name: ', user.get_name()
                print '\t\tAccount Balance : ', user.get_balance()
                user_list.remove(user)
                break
        else:
            print '*** Account does not exist ***'

    elif ch == 6:
        print('\n You are exiting the process')
        dummy_var = False
