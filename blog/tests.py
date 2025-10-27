from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
    def test_create_draft_post(self):
        """Test that a draft post can be created"""
        post = Post.objects.create(
            title='Test Draft Post',
            slug='test-draft-post',
            author=self.user,
            content='This is a draft post content',
            status='draft'
        )
        self.assertEqual(post.status, 'draft')
        self.assertEqual(post.title, 'Test Draft Post')
        
    def test_create_published_post(self):
        """Test that a published post can be created"""
        post = Post.objects.create(
            title='Test Published Post',
            slug='test-published-post',
            author=self.user,
            content='This is a published post content',
            status='published'
        )
        self.assertEqual(post.status, 'published')
        
    def test_default_status_is_draft(self):
        """Test that default status is draft"""
        post = Post.objects.create(
            title='Test Default Post',
            slug='test-default-post',
            author=self.user,
            content='This post should default to draft'
        )
        self.assertEqual(post.status, 'draft')


class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create draft and published posts
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='This is a draft',
            status='draft'
        )
        
        self.published_post = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=self.user,
            content='This is published',
            status='published'
        )
        
    def test_post_list_only_shows_published(self):
        """Test that only published posts appear in the list view"""
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Post')
        self.assertNotContains(response, 'Draft Post')
        
    def test_draft_post_not_accessible(self):
        """Test that draft posts are not accessible via detail view"""
        response = self.client.get(reverse('blog:post_detail', args=['draft-post']))
        self.assertEqual(response.status_code, 404)
        
    def test_published_post_accessible(self):
        """Test that published posts are accessible via detail view"""
        response = self.client.get(reverse('blog:post_detail', args=['published-post']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Post')
