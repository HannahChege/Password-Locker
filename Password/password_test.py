import unittest # Importing the unittest module
from password import User # Importing the user class

 class TestUser(unittest.TestCase):

     '''
     Test class that defines test cases for the user class behaviours.

     Args:
         unittest.Testcase: Testcase class that helps in creating test cases
     '''
         # Items up here .......

            def setUp(self):
                '''
                Set up method to run before each test cases.
                '''
                self.new_user = User("a","b","c") # create user object


            def test_init(self):
                '''
                test_init test case to test if the object is initialized properly
                '''

                self.assertEqual(self.new_user.first_name,"a")
                self.assertEqual(self.new_user.last_name,"b")
                self.assertEqual(self.new_user.password,"c")



if __name__ == '__main__':
    unittest.main()