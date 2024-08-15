import json

def file(x='a'):
    try:
        with open('file1.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        print('No data file found, starting fresh.')

    if x == 'a':
        username = input('Enter your desired username: ')
        password = input('Create a password: ')

        if username in data:
            print("This username already exists. Please try a different one.")
        else:
            data[username] = password
            with open('file1.json', 'w') as f:
                json.dump(data, f)
            print("You have successfully signed up!")

    elif x == 'r':
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        if username in data and data[username] == password:
            print("Welcome back! Login successful.")
        else:
            print("Incorrect username or password. Please try again.")

print('1) Signup')
print('2) Login')
print('3) Exit')

while True:
    choice = int(input('Please choose an option: '))
    if choice == 1:
        file()
    elif choice == 2:
        file(x='r')
    elif choice == 3:
        break
    else:
        print('Invalid option. Please enter 1, 2, or 3.')
