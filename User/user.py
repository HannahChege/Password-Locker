class User:
    """
    Class that generates new instances of Users
    """

       User_list = [] # Empty user list

 def __init__(self, first_name, last_name, password, email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            password: New contact password.
            email : New contact email address.
        '''