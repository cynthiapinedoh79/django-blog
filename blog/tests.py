from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Test content')
        self.assertEqual(self.post.author, self.user)
        self.assertFalse(self.post.published)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_post_list_view(self):
        """Test that logged-in users can read blog posts (AC2)"""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """Test that logged-in users can read a blog post (AC2)"""
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test content')

    def test_post_create_view_requires_login(self):
        """Test that post creation requires login"""
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_post_create_view_authenticated(self):
        """Test that logged-in users can create a blog post (AC1)"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_post_request(self):
        """Test creating a post via POST request (AC1)"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'content': 'New content',
            'published': 'on'
        })
        self.assertEqual(Post.objects.count(), 2)
        new_post = Post.objects.get(title='New Post')
        self.assertEqual(new_post.content, 'New content')
        self.assertTrue(new_post.published)

    def test_post_update_view_requires_login(self):
        """Test that post update requires login"""
        response = self.client.get(reverse('post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_post_update_view_authenticated(self):
        """Test that logged-in users can update a blog post (AC3)"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_update_post_request(self):
        """Test updating a post via POST request (AC3)"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_update', args=[self.post.pk]), {
            'title': 'Updated Post',
            'content': 'Updated content',
            'published': 'on'
        })
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.content, 'Updated content')
        self.assertTrue(self.post.published)

    def test_post_delete_view_requires_login(self):
        """Test that post deletion requires login"""
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_post_delete_view_authenticated(self):
        """Test that logged-in users can delete a blog post (AC4)"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_delete_post_request(self):
        """Test deleting a post via POST request (AC4)"""
        self.client.login(username='testuser', password='testpass123')
        post_id = self.post.pk
        response = self.client.post(reverse('post_delete', args=[post_id]))
        self.assertEqual(Post.objects.filter(pk=post_id).count(), 0)
        self.assertRedirects(response, reverse('post_list'))
