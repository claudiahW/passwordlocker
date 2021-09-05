import random
from user import user

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = user(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()    

def main():
    while True:
        print("Welcome to password locker!")
        print('\n')
        print("select a short code to use for navigation.to create a new user use 'nu':to login use lg:to exit  use ex:")
        short_code = input().lower()
        print('\n')

    if short_code =='nu':
        print('create username')
        created_user_name = input()

        print('create password')
        created_user_password =input()

        print('confirm your password')
        confirm_password = input()


        while confirm_password != created_user_password:
            print ('ooops password is incorrect!')
            print('enter your password')
            created_user_password = input()
            print('confirm your password')
            confirm_password =()
        else:
            print(f'congratulations {created_user_password}! account creation successful')
            print('\n')
            print('proceed to login')
            print('Username')
            entered_username = input()
            print('your password')
            entered_password = input()

        while entered_username !=created_user_name or entered_password != created_user_password:
            print('invalid username or password')
            print('Username')
            entered_username =input()
            print('your password')
            entered_password = input()
            







        
