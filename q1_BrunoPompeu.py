balance = 5000

withdraw = lambda balance, amount: print("Your balance is:", balance - amount) if amount <= balance else print("Insufficient funds. Your balance is:", balance)
deposit = lambda balance, amount: balance + amount
display_balance = lambda balance: print("Your balance is:", balance)

options = {
    1: lambda: withdraw(balance, int(input("Enter the amount to withdraw: "))),
    2: lambda: print("Your balance is:", deposit(balance, int(input("Enter the amount to deposit: ")))),
    3: lambda: display_balance(balance),
    'default': lambda: print("Invalid option")
}

print("Welcome to Santander Bank")
print("Please choose an option:")
print("1 - Withdraw")
print("2 - Deposit")
print("3 - Balance")

selectedOption = int(input("Option: "))
options.get(selectedOption, options['default'])()
