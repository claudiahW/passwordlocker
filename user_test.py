import unittest # Importing the unittest module
from user import User # Importing the user class

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
        self.new_user = User("Claudia","Wanjiru","1234") # create contact object


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Claudia")
        self.assertEqual(self.new_user.last_name,"Wanjiru")
        self.assertEqual(self.new_user.password,"1234")
        


if __name__ == '__main__':
    unittest.main()
    