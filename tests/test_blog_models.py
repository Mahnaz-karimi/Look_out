from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.utils import timezone


class BlogModelTest(TestCase):

    def setUp(self):
        self.title = 'post_title'
        self.content = 'post_content_Test'
        self.author = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.author.save()

        self.post = Post.objects.create(title=self.title, content=self.content, author=self.author)
        self.comment = Comment.objects.create(content='comment_content_Test', author=self.author,
                                              post=self.post)
        self.post.save()
        self.comment.save()

    # Test that post has title of type str
    def test_post_has_title(self):
        self.assertEqual(self.post.title, 'post_title')

    def test_post_title_type(self):
        self.assertIsInstance(self.post.title, str)

    # Test that post has content of type str
    def test_post_content_type(self):
        self.assertIsInstance(self.post.content, str)

    # Test postens tid er lige nutid i det nedstående format
    def test_post_created_date(self):
        self.assertEqual(str(self.post.date_posted.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]),
                         str(timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]))

    # Test that post author is instance of User
    def test_post_has_author(self):
        self.assertIsInstance(self.post.author, User)

    # Test that post has author
    def test_post_has_author(self):
        self.assertEqual(self.post.author, self.author)

    # Test that comment is the same post
    def test_post_comment_is_same_of_post(self):
        self.assertEqual(self.comment.post, self.post)

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_comment_has_content(self):
        self.assertEqual(str(self.comment.content), "comment_content_Test")

    def test_comment_instance_str(self):
        self.assertIsInstance(self.comment, Comment)

    # Test that post has content of type str
    def test_comment_content_type(self):
        self.assertIsInstance(self.comment.content, str)
