import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = User("a", "b", "c", "d")  # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "a")
        self.assertEqual(self.new_contact.last_name, "b")
        self.assertEqual(self.new_contact.password, "c")
        self.assertEqual(self.new_contact.email, "d")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)
if __name__ == '__main__':
    unittest.main()