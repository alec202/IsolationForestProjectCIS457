from ad_view_function import user
from login_function import login
#main function that stimulates the company's login system and ad viewing system
if __name__ == '__main__':
    while True:
        print("Please choose a function to stimulate")
        command = input("login | view ad | exit\n")
        if command == 'login':
            print("Enter your IP address to login")
            ip = input()
            login(ip)
        elif command == 'view ad':
            user()
        elif command == 'exit':
            break
