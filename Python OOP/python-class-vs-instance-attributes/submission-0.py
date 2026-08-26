class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
        



# TODO: Create two accounts
account_one = BankAccount("Alice", 1000)
account_two = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format

print(f"Alice's balance: ${account_one.balance}")
print(f"Bob's balance: ${account_two.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")



