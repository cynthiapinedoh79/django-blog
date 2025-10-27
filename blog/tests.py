from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(str(self.post), 'Test Post')
        self.assertEqual(self.post.status, 1)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test comment',
            approved=False
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test comment')
        self.assertFalse(self.comment.approved)
        self.assertEqual(str(self.comment), f'Comment by testuser on Test Post')

    def test_comment_approval(self):
        """Test AC1: Comments can be approved"""
        self.assertFalse(self.comment.approved)
        self.comment.approved = True
        self.comment.save()
        self.assertTrue(self.comment.approved)

    def test_comment_reply(self):
        """Test AC2: Users can reply to comments"""
        reply = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Reply to comment',
            approved=True,
            parent=self.comment
        )
        self.assertEqual(reply.parent, self.comment)
        self.assertIn(reply, self.comment.replies.all())

    def test_conversation_thread(self):
        """Test AC3: Multiple comments create conversation thread"""
        self.comment.approved = True
        self.comment.save()
        
        reply1 = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='First reply',
            approved=True,
            parent=self.comment
        )
        reply2 = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Second reply',
            approved=True,
            parent=self.comment
        )
        
        replies = self.comment.get_replies()
        self.assertEqual(replies.count(), 2)
        self.assertIn(reply1, replies)
        self.assertIn(reply2, replies)


class PostListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test content')

    def test_comment_submission_requires_login(self):
        """Test that unauthenticated users cannot submit comments"""
        response = self.client.post(
            reverse('post_detail', args=['test-post']),
            {'content': 'Test comment'}
        )
        self.assertEqual(Comment.objects.count(), 0)

    def test_authenticated_user_can_comment(self):
        """Test that authenticated users can submit comments"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('post_detail', args=['test-post']),
            {'content': 'Test comment'}
        )
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.content, 'Test comment')
        self.assertFalse(comment.approved)  # AC1: Comments require approval

    def test_only_approved_comments_displayed(self):
        """Test AC1: Only approved comments are displayed"""
        # Create unapproved comment
        Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Unapproved comment',
            approved=False
        )
        # Create approved comment
        Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Approved comment',
            approved=True
        )
        
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertContains(response, 'Approved comment')
        self.assertNotContains(response, 'Unapproved comment')

    def test_reply_to_comment(self):
        """Test AC2: Users can reply to comments"""
        parent_comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Parent comment',
            approved=True
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('post_detail', args=['test-post']),
            {
                'content': 'Reply to parent',
                'parent_id': parent_comment.id
            }
        )
        
        self.assertEqual(Comment.objects.count(), 2)
        reply = Comment.objects.last()
        self.assertEqual(reply.parent, parent_comment)
        self.assertEqual(reply.content, 'Reply to parent')


class CommentAdminTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@test.com'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test comment',
            approved=False
        )

    def test_comment_approval_in_admin(self):
        """Test that admin can approve comments (AC1)"""
        self.assertFalse(self.comment.approved)
        self.comment.approved = True
        self.comment.save()
        self.assertTrue(self.comment.approved)
