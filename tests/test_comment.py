import unittest
from app.models import User,Post,Comment

class TestComment(unittest.TestCase):
    """
    This is where we will run all the tests for the Comment model
    """

    def setUp(self):    
        """
        This will create a new instance of User, Post and Comment before each test
        """

        self.new_user = User(name = "sharonne")
        self.new_post = Post(title = "hello", user = self.new_user)
        self.new_comment = Comment(content = "winning", user = self.new_user, post = self.new_post)

    def tearDown(self):
        """
        Will clear the db after each test
        """
        User.query.delete()
        Post.query.delete()
        Comment.query.delete()

    def test_instance(self):
        """
        Will test whether the new comment is an instance of the Comment model
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        """
        Will test whether the comment is instantiated correctly
        """
        self.assertEquals(self.new_comment.post_comment, "winning")

  