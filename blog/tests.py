from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class PostModelTest(TestCase):
    """Tests for the Post model"""
    
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
        """Test that a post can be created"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.status, 1)
    
    def test_post_str_method(self):
        """Test the string representation of a post"""
        self.assertEqual(str(self.post), 'Test Post')


class CommentModelTest(TestCase):
    """Tests for the Comment model"""
    
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
            name='Test Commenter',
            email='test@example.com',
            body='Test comment body',
            approved=True
        )
    
    def test_comment_creation(self):
        """Test that a comment can be created"""
        self.assertEqual(self.comment.name, 'Test Commenter')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.body, 'Test comment body')
        self.assertEqual(self.comment.post, self.post)
        self.assertTrue(self.comment.approved)
    
    def test_comment_str_method(self):
        """Test the string representation of a comment"""
        self.assertIn('Test comment body', str(self.comment))
        self.assertIn('Test Commenter', str(self.comment))


class PostListViewTest(TestCase):
    """Tests for the PostList view"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        # Create published posts
        for i in range(3):
            Post.objects.create(
                title=f'Test Post {i}',
                slug=f'test-post-{i}',
                author=self.user,
                content=f'Test content {i}',
                status=1
            )
        # Create draft post (should not appear)
        Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='Draft content',
            status=0
        )
    
    def test_post_list_view_status_code(self):
        """Test that the post list view returns 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_view_template(self):
        """Test that the post list view uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/post_list.html')
    
    def test_post_list_only_shows_published(self):
        """Test that only published posts are shown"""
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['object_list']), 3)
        for post in response.context['object_list']:
            self.assertEqual(post.status, 1)


class PostDetailViewTest(TestCase):
    """Tests for the PostDetail view"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )
        # Create approved comments
        for i in range(3):
            Comment.objects.create(
                post=self.post,
                name=f'Commenter {i}',
                email=f'test{i}@example.com',
                body=f'Test comment {i}',
                approved=True
            )
        # Create unapproved comment (should not appear)
        Comment.objects.create(
            post=self.post,
            name='Unapproved User',
            email='unapproved@example.com',
            body='Unapproved comment',
            approved=False
        )
    
    def test_post_detail_view_status_code(self):
        """Test that the post detail view returns 200"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_view_template(self):
        """Test that the post detail view uses the correct template"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertTemplateUsed(response, 'blog/post_detail.html')
    
    def test_post_detail_view_shows_approved_comments(self):
        """Test that only approved comments are shown"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(len(response.context['comments']), 3)
        for comment in response.context['comments']:
            self.assertTrue(comment.approved)
    
    def test_post_detail_view_comment_count(self):
        """Test that the comment count is correct"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.context['comment_count'], 3)
    
    def test_post_detail_view_contains_comment_text(self):
        """Test that the view contains comment text"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertContains(response, 'Test comment 0')
        self.assertContains(response, 'Commenter 1')
        self.assertNotContains(response, 'Unapproved comment')
    
    def test_post_detail_view_shows_comment_section(self):
        """Test that the comment section is displayed"""
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertContains(response, '3 Comments')


class AdminCommentTest(TestCase):
    """Tests for admin comment functionality"""
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
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
            name='Test Commenter',
            email='test@example.com',
            body='Test comment',
            approved=False
        )
    
    def test_admin_can_view_comments(self):
        """Test that admin can access the comment list"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/admin/blog/comment/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_can_view_unapproved_comments(self):
        """Test that admin can see unapproved comments"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/admin/blog/comment/')
        self.assertContains(response, 'Test comment')
