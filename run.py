import random
from user import user

def create_user(username,password):
    '''
    Function to create a new contact
    '''
    new_user = user(username,password)
    return new_user
