import unittest
from app.models import Post,User,Comment

class TestPost(unittest.TestCase):
    """
    This is the class which we will use to do tests for the post
    """

    def setUp(self):
        """
        This will create an instance of the User and Post before each test case
        """
        self.new_user = User(username = "sharonne")
        self.new_post = Post(title = "hello", user = self.new_user)

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        Post.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_instance(self):
        """
        Will test whether the new_post is an instance of Post
        """
        self.assertTrue(isinstance(self.new_post, Post))

    def test_init(self):
        """
        Will test whether the new_post is instantiated correctly
        """

        self.assertEqual(self.new_post.title, "hello")

    def test_save_post(self,post):
        """
        Will test whether the post is saved into the database
        """
        self.new_post.save_post()
        post= Post.query.all()
        self.assertTrue(len(post) > 0)

    def test_relationship_user(self):
        """
        Will test whether the post is correctly related to the user who posted it
        """
        user = self.new_post.user.name
        self.assertTrue(user == "sharonne")