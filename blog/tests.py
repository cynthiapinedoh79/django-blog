from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class UserRegistrationTests(TestCase):
    """Test user registration functionality"""

    def setUp(self):
        self.client = Client()

    def test_user_can_access_registration_page(self):
        """Test that users can access the registration page"""
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_register_with_email(self):
        """Test that users can register with an email address"""
        response = self.client.post(reverse('account_signup'), {
            'email': 'testuser@example.com',
            'password1': 'testpass123!@#',
            'password2': 'testpass123!@#',
        })
        # Should redirect after successful registration
        self.assertEqual(response.status_code, 302)
        
        # Check user was created
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())


class UserLoginTests(TestCase):
    """Test user login functionality"""

    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_can_access_login_page(self):
        """Test that users can access the login page"""
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_login_after_registration(self):
        """Test that users can login with their credentials"""
        response = self.client.post(reverse('account_login'), {
            'login': 'test@example.com',
            'password': 'testpass123',
        })
        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)


class CommentTests(TestCase):
    """Test commenting functionality"""

    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )

    def test_logged_in_user_can_comment(self):
        """Test that logged-in users can comment on posts"""
        # Login the user
        self.client.login(username='testuser', password='testpass123')
        
        # Submit a comment
        response = self.client.post(
            reverse('post_detail', kwargs={'slug': 'test-post'}),
            {'content': 'Test comment'}
        )
        
        # Should redirect after successful comment
        self.assertEqual(response.status_code, 302)
        
        # Check comment was created
        self.assertTrue(Comment.objects.filter(
            post=self.post,
            author=self.user,
            content='Test comment'
        ).exists())

    def test_anonymous_user_cannot_comment(self):
        """Test that anonymous users cannot comment"""
        # Try to submit a comment without logging in
        response = self.client.post(
            reverse('post_detail', kwargs={'slug': 'test-post'}),
            {'content': 'Test comment'}
        )
        
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
        
        # Check no comment was created
        self.assertFalse(Comment.objects.filter(content='Test comment').exists())

    def test_comment_form_displayed_for_authenticated_users(self):
        """Test that the comment form is displayed for authenticated users"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('post_detail', kwargs={'slug': 'test-post'}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leave a comment')

    def test_login_prompt_displayed_for_anonymous_users(self):
        """Test that a login prompt is displayed for anonymous users"""
        response = self.client.get(reverse('post_detail', kwargs={'slug': 'test-post'}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please')
        self.assertContains(response, 'login')


class PostModelTests(TestCase):
    """Test Post model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_post_creation(self):
        """Test that posts can be created"""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(post.author, self.user)


class CommentModelTests(TestCase):
    """Test Comment model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )

    def test_comment_creation(self):
        """Test that comments can be created"""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test comment'
        )
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertIn('testuser', str(comment))
