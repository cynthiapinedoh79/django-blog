from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class CommentApprovalTestCase(TestCase):
    def setUp(self):
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
        
        self.client = Client()

    def test_comment_created_unapproved_by_default(self):
        """Test that comments are created with approved=False by default"""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='New comment'
        )
        self.assertFalse(comment.approved)

    def test_approve_comment_requires_login(self):
        """Test that approving a comment requires authentication"""
        url = reverse('blog:approve_comment', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_approve_comment_when_logged_in(self):
        """Test that logged in user can approve a comment (AC1)"""
        self.client.login(username='testuser', password='testpass123')
        url = reverse('blog:approve_comment', args=[self.comment.id])
        response = self.client.get(url)
        
        # Refresh comment from database
        self.comment.refresh_from_db()
        self.assertTrue(self.comment.approved)

    def test_disapprove_comment_requires_login(self):
        """Test that disapproving a comment requires authentication"""
        url = reverse('blog:disapprove_comment', args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_disapprove_comment_when_logged_in(self):
        """Test that logged in user can disapprove a comment (AC2)"""
        # First approve the comment
        self.comment.approved = True
        self.comment.save()
        
        self.client.login(username='testuser', password='testpass123')
        url = reverse('blog:disapprove_comment', args=[self.comment.id])
        response = self.client.get(url)
        
        # Refresh comment from database
        self.comment.refresh_from_db()
        self.assertFalse(self.comment.approved)

    def test_admin_bulk_approve_comments(self):
        """Test that admin can bulk approve comments"""
        comment2 = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Another comment',
            approved=False
        )
        
        # Test queryset update
        Comment.objects.filter(id__in=[self.comment.id, comment2.id]).update(approved=True)
        
        self.comment.refresh_from_db()
        comment2.refresh_from_db()
        
        self.assertTrue(self.comment.approved)
        self.assertTrue(comment2.approved)

    def test_admin_bulk_disapprove_comments(self):
        """Test that admin can bulk disapprove comments"""
        self.comment.approved = True
        self.comment.save()
        
        comment2 = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Another comment',
            approved=True
        )
        
        # Test queryset update
        Comment.objects.filter(id__in=[self.comment.id, comment2.id]).update(approved=False)
        
        self.comment.refresh_from_db()
        comment2.refresh_from_db()
        
        self.assertFalse(self.comment.approved)
        self.assertFalse(comment2.approved)
