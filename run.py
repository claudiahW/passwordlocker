import string
from random import *
from user import User
from user import Details
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()
def create_account(accountusername,accountname,accountpassword):
    newaccount= Details(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return Details.find_by_number(number)
def display_accounts():
    return Details.display_accounts()
def main():
        while True:
            print("Welcome to Password Locker!Sign up or Log in to continue")
            print("SignUp -or- LogIn")
            option=input()
            if option == "SignUp":
                print("Create Account")
                print("-"*10)
                print("Enter First Name..")
                firstname=input()
                print("Enter Last Name..")
                lastname=input()
                print("Set your username..")
                username=input()
                print("Set your password..")
                userpassword=input()
                save_user(create_user(firstname,lastname,username,userpassword))
                print("Account creation succesful!Here are your details:")
                print("-"*10)
                print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
                print("\nUse your details to LogIn")
                print("\n \n")
                # for user in display_users():
                #     print(f"{user.firstname} {user.lastname}.....{user.username}")
            elif option =="LogIn":
                print("Username..")
                loginUsername=input()
                print("Password..")
                loginPassword=input()
                if find_user(loginPassword):
                    print("\n")
                    print("Would you like to Add an account or View  current accounts?")
                    print("-"*60)
                    print("AddAccount -or- ViewAccounts")
                    choose= input()
                    print("\n")
                    if choose == "AddAccount":
                        print("Add Details Account")
                        print("-"*25)
                        accountusername=loginUsername
                        print("Account Name")
                        accountname=input()
                        print("\n")
                        print("Generate automatic password(generate) or Create new password(create)?")
                        decision=input()
                        if decision=="generate":
                            characters=string.ascii_letters + string.digits
                            accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                            print(f"Password: {accountpassword}")
                        elif decision=="create":
                            print("Enter your Password")
                            accountpassword=input()
                        else:
                            print("Invalid Choice,try again")
                        save_account(create_account(accountusername,accountname,accountpassword))
                        print("\n")
                        print(f"Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")
                    elif choose == "ViewAccounts":
                        if find_account(accountusername):
                            print("Here are your accounts: ")
                            print("-"*25)
                            for user in display_accounts():
                                print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
                        else:
                            print("Invalid details!")
                    else:
                        print("Kindly try again!")
                        print("\n")
                else:
                    print("Incorrect username or password,please try again!")
                    print("\n")
            else:
                print("Kindly choose a valid option")
                print("\n")
if __name__ == '__main__':
     main()





