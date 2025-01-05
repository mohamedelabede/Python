class BankAccount:
    def __init__(self, account_number, holder_name, account_type, balance=0.0):
      
        self.account_number = account_number  # Unique account number
        self.holder_name = holder_name  # Account holder's name
        self.account_type = account_type  # Account type (e.g., 'Savings', 'Checking')
        self.balance = balance  # Account balance, default is 0.0
        self.transaction_history = []  # List to hold transaction history
    
    def deposit(self, amount):
      
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}. Current balance: ${self.balance}")
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
      
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}. Current balance: ${self.balance}")
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
    
    def check_balance(self):
        
        print(f"Current balance: ${self.balance}")
        return self.balance
    
    def get_account_details(self):
       
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Type: {self.account_type}")
        return {
            "Account Number": self.account_number,
            "Account Holder": self.holder_name,
            "Account Type": self.account_type
        }
    
    def get_transaction_history(self):
        
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")
    
# Example Usage
if __name__ == "__main__":
    # Creating a bank account for a user
    account1 = BankAccount(account_number="123456789", holder_name="John Doe", account_type="Savings")
    
    # Deposit some money into the account
    account1.deposit(500)
    
    # Withdraw some money
    account1.withdraw(200)
    
    # Checking the balance
    account1.check_balance()
    
    # Getting account details
    account1.get_account_details()
    
    # Getting transaction history
    account1.get_transaction_history()

    # Attempting a withdrawal with insufficient funds
    account1.withdraw(400)
    
    # Final balance check
    account1.check_balance()
