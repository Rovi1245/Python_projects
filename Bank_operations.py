class Bank:
    bank_name = 'Central Bank of India'
    branch = '123,Mysore,Karnataka'
    
    def __init__(self,name,pan_no,address):
        self.name = name
        self.pan_no = pan_no
        self.address = address
        self.balance = 0
        print(f'Congratulations!! {self.name}, your account has created sucessfully')
        
        
    def deposit(self,amount):
        self.balance += amount
        print(f'The deposit of {amount} is sucessfull')
        
        
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance -= amount
            
    def ministatement(self):
        print(f'The account balance is {self.balance}')
        
        
print(f'Welcome to {Bank.bank_name}, branch {Bank.branch}')
print('Enter the following details: ')
name =input('Enter the name: ')
pan_no = input('Enter the pan number: ')
address = input('Enter the address: ')

b = Bank(name,pan_no,address)


while True:
    print('\nSelect the option below')
    print('\n1.Deposit\n2.Withdraw\n3.MiniStatement\n4.Stop')
    option = int(input(' '))
    
    
    if option == 1:
        amount = float(input('Enter the amount to deposit: '))
        b.deposit(amount)
        
    if option == 2:
        amount = float(input('Enter the amount to withdraw: '))
        b.withdraw(amount)
        
    if option == 3:
        b.ministatement()
        
    if option == 4:
        print(f'Thanks for choosing the {b.bank_name}')
        break
    
    else:
        print('Please select the valid option')
    
    