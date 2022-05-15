import unittest
from app.models import User,Post

class TestUsers(unittest.TestCase):
    """
    This is the class which we will use to do tests for the User
    """
    def setUp(self):
        """
        This will create an instance of the User before each test case
        """

        self.new_user = User(username = "sharonne", password = "atara")

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        User.query.delete()
        Post.query.delete()

    def test_instance(self):
        """
        Will test whether the new instance is an instance of the User model
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_init(self):
        """
        Will test whether the User model is instantiated correctly
        """
        self.assertEqual(self.new_user.username,"sharonne")

    def test_password_generate(self):
        """
        Will test whether a password is generated
        """
        self.assertTrue(self.new_user.password_hash is not None)
    
    def test_password_is_hashed(self):
        """
        Will test whether the password generated is not equal to the inputted password
        """
        self.assertTrue(self.new_user.password_hash is not "atara")

    def test_password_verifier(self):
        """
        Will test whether the user can decrypt the password with their password
        """
        self.assertTrue(self.new_user.verify_password("atara"))

    