from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    """Test the Post model."""
    
    def setUp(self):
        """Create a test user and post."""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is test content for the blog post.',
            status=1
        )
    
    def test_post_creation(self):
        """Test that a post is created correctly."""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.status, 1)
    
    def test_post_str(self):
        """Test the string representation of the post."""
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_get_absolute_url(self):
        """Test the get_absolute_url method."""
        self.assertEqual(self.post.get_absolute_url(), '/test-post/')


class PostListViewTest(TestCase):
    """Test the PostList view."""
    
    def setUp(self):
        """Create test users and posts."""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.published_post = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=self.user,
            content='This is a published post.',
            status=1
        )
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='This is a draft post.',
            status=0
        )
    
    def test_post_list_view_url(self):
        """Test that the post list view is accessible."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_view_url_by_name(self):
        """Test that the post list view is accessible by name."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_view_template(self):
        """Test that the correct template is used."""
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'blog/post_list.html')
    
    def test_post_list_only_shows_published(self):
        """Test that only published posts are shown."""
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'Published Post')
        self.assertNotContains(response, 'Draft Post')


class PostDetailViewTest(TestCase):
    """Test the PostDetail view - this is the key requirement for the issue."""
    
    def setUp(self):
        """Create test users and posts."""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.published_post = Post.objects.create(
            title='Published Post Detail',
            slug='published-post-detail',
            author=self.user,
            content='This is the full content of a published post that should be visible when clicked.',
            status=1
        )
        self.draft_post = Post.objects.create(
            title='Draft Post Detail',
            slug='draft-post-detail',
            author=self.user,
            content='This is a draft post that should not be accessible.',
            status=0
        )
    
    def test_post_detail_view_url(self):
        """Test that the post detail view is accessible via URL."""
        response = self.client.get(f'/{self.published_post.slug}/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_view_url_by_name(self):
        """Test that the post detail view is accessible by name."""
        response = self.client.get(reverse('post_detail', args=[self.published_post.slug]))
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_view_template(self):
        """Test that the correct template is used."""
        response = self.client.get(reverse('post_detail', args=[self.published_post.slug]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    
    def test_post_detail_shows_full_content(self):
        """Test that the full post content is displayed (AC1 requirement)."""
        response = self.client.get(reverse('post_detail', args=[self.published_post.slug]))
        self.assertContains(response, 'Published Post Detail')
        self.assertContains(response, 'This is the full content of a published post that should be visible when clicked.')
    
    def test_post_detail_shows_author_and_date(self):
        """Test that author and date information is displayed."""
        response = self.client.get(reverse('post_detail', args=[self.published_post.slug]))
        self.assertContains(response, 'testuser')
    
    def test_draft_post_not_accessible(self):
        """Test that draft posts are not accessible."""
        response = self.client.get(reverse('post_detail', args=[self.draft_post.slug]))
        self.assertEqual(response.status_code, 404)
    
    def test_clicking_post_title_redirects_to_detail(self):
        """Test that clicking a post title on the list page shows the detail view."""
        # Get the list page
        list_response = self.client.get(reverse('post_list'))
        self.assertEqual(list_response.status_code, 200)
        
        # Verify the link to detail page exists
        detail_url = reverse('post_detail', args=[self.published_post.slug])
        self.assertContains(list_response, f'href="{detail_url}"')
        
        # Follow the link to detail page
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, self.published_post.content)
