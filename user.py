import random
import string
class User:
    """
    Creates new user instances.
    """
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        """
        __init__ defines the properties of self.
        Args:
        firstname: User's first name
        lastname: User's last name
        username: New username
        password: New password
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        """
        save_user saves objects to the userslist.
        """
        User.userslist.append(self)
    def delete_user(self):
        """
        delete_user deletes a saved user from the userslist.
        """
        User.userslist.remove(self)
    @classmethod
    def display_users(cls):
        """
        display_user returns the userlist.
        """
        return cls.userslist
    @classmethod
    def find_by_number(cls,number):
        """
        Takes in username and returns a user that matches the phone number.
        Args:
        number: Phone number Returns: Contact of person that matches the number.
        """
        for user in cls.userslist:
            if user.password == number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return False
class Details:
    """
    Class that generates new details.
    """
    accounts=[]
    def __init__(self,accountusername,accountname,accountpassword):
        """
        __init__ method that helps us define properties for the self object.
        Args:
        accountusername: New Details accountusername
        accountname: New Details accountname
        accountpassword: New Details accountpassword
        """
        self.accountusername= accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
    def save_account(self):
        """
        save_account saves user into accounts
        """
        Details.accounts.append(self)
    def delete_account(self):
        """
        delete_account deletes a saved Detail from accounts
        """
        Details.accounts.remove(self)
    #Changes made here that might affect code
    @classmethod
    def display_accounts(cls):
        """
        display_account returns the accounts
        """
        for account in cls.accounts:
            return cls.accounts
    @classmethod
    def find_by_number(cls,number):
        """
        find_by_number takes in a number and returns a contact that matches that number
        Args:
        number: accountusername to search for Returns: Details of the user who matches the number.
        """
        for account in cls.accounts:
            if account.accountusername ==number:
                return account