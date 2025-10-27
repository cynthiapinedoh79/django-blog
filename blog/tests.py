from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        """Set up test user for the tests"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_create_draft_post(self):
        """Test creating a draft post"""
        post = Post.objects.create(
            title='Test Draft Post',
            slug='test-draft-post',
            author=self.user,
            content='This is a test draft post content',
            status=0  # Draft
        )
        self.assertEqual(post.status, 0)
        self.assertEqual(post.title, 'Test Draft Post')
        self.assertEqual(str(post), 'Test Draft Post')

    def test_draft_post_can_be_saved_and_retrieved(self):
        """Test that draft posts can be saved and retrieved later"""
        # Create draft post
        Post.objects.create(
            title='Draft to Finish Later',
            slug='draft-to-finish-later',
            author=self.user,
            content='Initial draft content',
            status=0  # Draft
        )
        
        # Retrieve the draft post
        draft_post = Post.objects.get(slug='draft-to-finish-later')
        self.assertEqual(draft_post.status, 0)
        self.assertEqual(draft_post.content, 'Initial draft content')
        
        # Update the draft post (finishing it later)
        draft_post.content = 'Updated draft content with more information'
        draft_post.save()
        
        # Verify the update was saved
        updated_post = Post.objects.get(slug='draft-to-finish-later')
        self.assertEqual(updated_post.content, 'Updated draft content with more information')
        self.assertEqual(updated_post.status, 0)  # Still a draft

    def test_draft_post_default_status(self):
        """Test that new posts default to draft status"""
        post = Post.objects.create(
            title='New Post',
            slug='new-post',
            author=self.user,
            content='New post content'
            # Note: status not explicitly set
        )
        self.assertEqual(post.status, 0)  # Should default to Draft

    def test_draft_vs_published_posts(self):
        """Test distinction between draft and published posts"""
        # Create a draft post
        draft = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='Draft content',
            status=0
        )
        
        # Create a published post
        published = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=self.user,
            content='Published content',
            status=1
        )
        
        # Verify they have different statuses
        self.assertEqual(draft.status, 0)
        self.assertEqual(published.status, 1)
        
        # Verify we can filter by status
        draft_posts = Post.objects.filter(status=0)
        published_posts = Post.objects.filter(status=1)
        
        self.assertEqual(draft_posts.count(), 1)
        self.assertEqual(published_posts.count(), 1)
        self.assertIn(draft, draft_posts)
        self.assertIn(published, published_posts)

