import unittest # Importing the unittest module
from user import user # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user =user("Claudia","1234") # create user object


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Claudia")
        self.assertEqual(self.new_user.password,"1234")

def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)
        
        

if __name__ == '__main__':
    unittest.main()
    