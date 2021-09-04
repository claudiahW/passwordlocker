class User:
    '''
class that generates a new user instance
    '''
user_list =[]

def __init__(self,user_name,password):
    self.user_name = user_name
    self.password = password

def save_user(self):
    '''
    saves users information

    '''  
  User.user_list.append(self)   

