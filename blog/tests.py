from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

# Create your tests here.


class PostListViewTest(TestCase):
    """Tests for the paginated post list view"""

    @classmethod
    def setUpTestData(cls):
        """Create test user and posts"""
        # Create a test user
        cls.test_user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )

        # Create 15 published posts for pagination testing
        for i in range(15):
            Post.objects.create(
                title=f'Test Post {i+1}',
                slug=f'test-post-{i+1}',
                author=cls.test_user,
                content=f'This is test post content {i+1}',
                excerpt=f'Test excerpt {i+1}',
                status=1  # Published
            )

        # Create 2 draft posts (should not appear in list)
        for i in range(2):
            Post.objects.create(
                title=f'Draft Post {i+1}',
                slug=f'draft-post-{i+1}',
                author=cls.test_user,
                content=f'This is draft post content {i+1}',
                status=0  # Draft
            )

    def test_view_url_exists_at_desired_location(self):
        """Test that the main page URL works"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test that the home URL name works"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Test that the correct template is used"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_pagination_is_six(self):
        """Test that pagination shows 6 posts per page"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['object_list']), 6)

    def test_lists_all_published_posts(self):
        """Test that all published posts are accessible via pagination"""
        # Get first page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        
        # Should have 3 pages (15 posts / 6 per page = 2.5 -> 3 pages)
        self.assertEqual(response.context['page_obj'].paginator.num_pages, 3)
        
        # Get second page
        response = self.client.get(reverse('home') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 6)
        
        # Get third page (should have 3 posts: 15 - 6 - 6 = 3)
        response = self.client.get(reverse('home') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)

    def test_only_published_posts_shown(self):
        """Test that only published posts are shown, not drafts"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
        # Get all posts across all pages
        all_posts = []
        for page in range(1, 4):  # 3 pages
            response = self.client.get(reverse('home') + f'?page={page}')
            all_posts.extend(response.context['object_list'])
        
        # Should have exactly 15 published posts (not 17 with drafts)
        self.assertEqual(len(all_posts), 15)
        
        # Verify no draft posts are in the list
        for post in all_posts:
            self.assertEqual(post.status, 1)  # Published status


class PostModelTest(TestCase):
    """Tests for the Post model"""

    @classmethod
    def setUpTestData(cls):
        """Create test user and post"""
        cls.test_user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )

        cls.test_post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=cls.test_user,
            content='Test content',
            excerpt='Test excerpt',
            status=1
        )

    def test_post_creation(self):
        """Test that a post is created correctly"""
        self.assertEqual(self.test_post.title, 'Test Post')
        self.assertEqual(self.test_post.slug, 'test-post')
        self.assertEqual(self.test_post.author, self.test_user)
        self.assertEqual(self.test_post.status, 1)

    def test_post_string_representation(self):
        """Test the string representation of a post"""
        self.assertEqual(str(self.test_post), 'Test Post')

    def test_post_ordering(self):
        """Test that posts are ordered by created_on descending"""
        # Create another post
        second_post = Post.objects.create(
            title='Second Post',
            slug='second-post',
            author=self.test_user,
            content='Second content',
            status=1
        )

        posts = Post.objects.all()
        # The second post (created later) should come first
        self.assertEqual(posts[0], second_post)
        self.assertEqual(posts[1], self.test_post)
