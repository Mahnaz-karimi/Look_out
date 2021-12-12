from django.test import TestCase
from blog.models import Post, Comment, Photo, Youtube, Category
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

        self.content = "test"
        self.video = "https://www.youtube.com/watch?v=Geq60OVyBPg&t=8s"
        self.youtube = Youtube.objects.create(content=self.content, video=self.video)

        self.description = "Java"
        self.category = Category.objects.create(name="Java");
        self.image = "default.jpg"
        self.photo = Photo.objects.create(description=self.description, category=self.category, image=self.image, author=self.author)

    # Test that post has title of type str
    def test_post_has_title(self):
        self.assertEqual(self.post.title, 'post_title')

    def test_post_title_type(self):
        self.assertIsInstance(self.post.title, str)

    def test_comment_has_content(self):
        self.assertEqual(str(self.comment.content), "comment_content_Test")

    # Test that post has content of type str
    def test_post_content_type(self):
        self.assertIsInstance(self.post.content, str)

    # Test postens tid er lige nutid i det nedstående format
    def test_post_created_date(self):
        self.assertEqual(str(self.post.date_posted.strftime('%Y-%m-%d %H:%M')[:-7]),
                         str(timezone.now().strftime('%Y-%m-%d %H:%M')[:-7]))

    # Test that post author is instance of User
    def test_post_has_author(self):
        self.assertIsInstance(self.post.author, User)

    # Test that post has author
    def test_post_author_is_same_author(self):
        self.assertEqual(self.post.author, self.author)

    # Test that comment is the same post
    def test_post_comment_is_same_of_post(self):
        self.assertEqual(self.comment.post, self.post)

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_comment_instance_(self):
        self.assertIsInstance(self.comment, Comment)

    # Test that comment has content of type str
    def test_comment_content_type(self):
        self.assertIsInstance(self.comment.content, str)

    # Test that comment author is instance of User
    def test_comment_has_author(self):
        self.assertIsInstance(self.comment.author, User)

    # Test that comment post is instance of post
    def test_comment_has_post(self):
        self.assertIsInstance(self.comment.post, Post)

    # Test that comment has post
    def test_post_comment_is_post(self):
        self.assertEqual(self.comment.post, self.post)

    # Test that photo has the same author
    def test_photo_author_is_same_author(self):
        self.assertEqual(self.photo.author, self.author)

    # Test that youtube has the same youtube adress
    def test_youtube_video_is_same_video(self):
        self.assertEqual(self.youtube.video, self.video)

    # Test that youtube has the same content
    def test_youtube_content_is_same_content(self):
        self.assertEqual(self.youtube.content, "test")
