register_user = lambda: open("users.txt", "a").write(f"{input('Enter the username: ')}:{input('Enter the password: ')}\n")

login = lambda: (
    lambda username, password:
        print("SUCCESS - Login successful.")
        if any(line.strip().split(":")[0] == username and line.strip().split(":")[1] == password for line in open("users.txt", "r"))
        else print("FAILURE - Login failed. Check your username and password.")
    )(input("Enter the username: "), input("Enter the password: "))

options = {
    '1': register_user,
    '2': login,
}

print("1 - Register user")
print("2 - Login")
option = input("Option: ")
options.get(option, lambda: print("Invalid option. Try again."))()