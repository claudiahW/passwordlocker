class user:
    '''
    its a class that generates a new instance of users
    '''
    user_list = []
    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password
    def save_user(self):
        '''
        saves account details of the user information
        '''    
        user.user_list.append(self)