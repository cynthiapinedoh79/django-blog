from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class CommentApprovalTestCase(TestCase):
    """Test cases for comment approval functionality"""
    
    def setUp(self):
        """Set up test data"""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )
        
        # Create a test comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test comment',
            approved=False
        )
    
    def test_comment_created_unapproved(self):
        """Test that comments are created as unapproved by default"""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Another test comment'
        )
        self.assertFalse(comment.approved)
    
    def test_approve_comment(self):
        """Test approving a comment"""
        self.assertFalse(self.comment.approved)
        self.comment.approve()
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)
    
    def test_disapprove_comment(self):
        """Test disapproving a comment"""
        self.comment.approved = True
        self.comment.save()
        self.assertTrue(self.comment.approved)
        
        self.comment.disapprove()
        self.comment.refresh_from_db()
        self.assertFalse(self.comment.approved)
    
    def test_comment_str_representation(self):
        """Test string representation of comment"""
        expected_str = f'Comment by {self.user.username} on {self.post.title}'
        self.assertEqual(str(self.comment), expected_str)


class PostModelTestCase(TestCase):
    """Test cases for Post model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_post_creation(self):
        """Test creating a post"""
        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.author, self.user)
    
    def test_post_str_representation(self):
        """Test string representation of post"""
        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )
        self.assertEqual(str(post), 'Test Post')
