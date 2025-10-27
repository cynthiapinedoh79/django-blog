from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    """Test cases for the Post model"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post content.',
            status=1
        )

    def test_post_creation(self):
        """Test that a post can be created"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.status, 1)

    def test_post_str_method(self):
        """Test the string representation of the post"""
        self.assertEqual(str(self.post), 'Test Post')


class PostListViewTest(TestCase):
    """Test cases for the PostList view"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create published posts
        for i in range(3):
            Post.objects.create(
                title=f'Published Post {i}',
                slug=f'published-post-{i}',
                author=self.user,
                content=f'Content for published post {i}',
                status=1
            )
        # Create draft post
        Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='Draft content',
            status=0
        )

    def test_post_list_view_status_code(self):
        """Test that the post list view returns a 200 status code"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_uses_correct_template(self):
        """Test that the post list view uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_list_shows_only_published_posts(self):
        """Test that only published posts are shown in the list"""
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['object_list']), 3)
        for post in response.context['object_list']:
            self.assertEqual(post.status, 1)


class PostDetailViewTest(TestCase):
    """Test cases for the PostDetail view"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.published_post = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=self.user,
            content='This is published content.',
            status=1
        )
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='This is draft content.',
            status=0
        )

    def test_post_detail_view_status_code_for_published_post(self):
        """Test that the post detail view returns a 200 status code for published posts"""
        response = self.client.get(reverse('post_detail', args=['published-post']))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_uses_correct_template(self):
        """Test that the post detail view uses the correct template"""
        response = self.client.get(reverse('post_detail', args=['published-post']))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_view_shows_correct_post(self):
        """Test that the post detail view shows the correct post"""
        response = self.client.get(reverse('post_detail', args=['published-post']))
        self.assertEqual(response.context['post'].title, 'Published Post')
        self.assertEqual(response.context['post'].slug, 'published-post')

    def test_post_detail_view_404_for_draft_post(self):
        """Test that the post detail view returns 404 for draft posts"""
        response = self.client.get(reverse('post_detail', args=['draft-post']))
        self.assertEqual(response.status_code, 404)

    def test_post_detail_view_404_for_nonexistent_post(self):
        """Test that the post detail view returns 404 for non-existent posts"""
        response = self.client.get(reverse('post_detail', args=['nonexistent-post']))
        self.assertEqual(response.status_code, 404)

