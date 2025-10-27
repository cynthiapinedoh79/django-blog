from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class CommentEditDeleteTestCase(TestCase):
    """Test cases for comment edit and delete functionality"""

    def setUp(self):
        """Set up test data"""
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='testpass123')
        self.user2 = User.objects.create_user(username='user2', password='testpass123')
        
        # Create a post
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user1
        )
        
        # Create a comment by user1
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user1,
            content='This is a test comment.'
        )
        
        self.client = Client()

    def test_comment_edit_by_author(self):
        """Test that a comment author can edit their comment"""
        self.client.login(username='user1', password='testpass123')
        
        # Get the edit page
        response = self.client.get(reverse('comment_edit', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit Comment')
        
        # Post updated content
        response = self.client.post(
            reverse('comment_edit', args=[self.comment.pk]),
            {'content': 'Updated comment content'}
        )
        
        # Check redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[self.post.pk]))
        
        # Check comment was updated
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment content')

    def test_comment_edit_by_non_author(self):
        """Test that a non-author cannot edit another user's comment"""
        self.client.login(username='user2', password='testpass123')
        
        # Try to get the edit page
        response = self.client.get(reverse('comment_edit', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 403)
        
        # Try to post updated content
        response = self.client.post(
            reverse('comment_edit', args=[self.comment.pk]),
            {'content': 'Trying to update someone else\'s comment'}
        )
        self.assertEqual(response.status_code, 403)
        
        # Check comment was not updated
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'This is a test comment.')

    def test_comment_edit_unauthenticated(self):
        """Test that unauthenticated users cannot edit comments"""
        response = self.client.get(reverse('comment_edit', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_comment_delete_by_author(self):
        """Test that a comment author can delete their comment"""
        self.client.login(username='user1', password='testpass123')
        
        # Get the delete confirmation page
        response = self.client.get(reverse('comment_delete', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete Comment')
        
        # Post to delete
        response = self.client.post(reverse('comment_delete', args=[self.comment.pk]))
        
        # Check redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[self.post.pk]))
        
        # Check comment was deleted
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_comment_delete_by_non_author(self):
        """Test that a non-author cannot delete another user's comment"""
        self.client.login(username='user2', password='testpass123')
        
        # Try to get the delete page
        response = self.client.get(reverse('comment_delete', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 403)
        
        # Try to post to delete
        response = self.client.post(reverse('comment_delete', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 403)
        
        # Check comment still exists
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_comment_delete_unauthenticated(self):
        """Test that unauthenticated users cannot delete comments"""
        response = self.client.get(reverse('comment_delete', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_post_detail_shows_edit_delete_links_for_author(self):
        """Test that edit/delete links are shown to comment author"""
        self.client.login(username='user1', password='testpass123')
        
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit')
        self.assertContains(response, 'Delete')

    def test_post_detail_hides_edit_delete_links_for_non_author(self):
        """Test that edit/delete links are hidden from non-authors"""
        self.client.login(username='user2', password='testpass123')
        
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        # Check that the edit/delete links are not shown in comment actions div
        content = response.content.decode()
        self.assertNotIn(f'href="{reverse("comment_edit", args=[self.comment.pk])}"', content)
        self.assertNotIn(f'href="{reverse("comment_delete", args=[self.comment.pk])}"', content)
