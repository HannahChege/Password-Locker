class User:
    """
    Class that generates new instances of Users
    """

    user_list = [] #Empty user list
    def _init_(self,first_name,last_name,password):

        #docstrings removed for simplicity

         self.first_name = first_name
         self.last_name  =  last_name
         self.password   =  password