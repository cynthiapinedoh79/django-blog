from django.test import TestCase
from django.urls import reverse
from .models import About


class AboutModelTest(TestCase):
    """Test the About model"""

    def test_about_creation(self):
        """Test creating an About object"""
        about = About.objects.create(
            title="Test About",
            content="Test content"
        )
        self.assertEqual(about.title, "Test About")
        self.assertEqual(about.content, "Test content")
        self.assertIsNotNone(about.updated_on)

    def test_about_str_method(self):
        """Test the string representation of About"""
        about = About.objects.create(
            title="Test About",
            content="Test content"
        )
        self.assertEqual(str(about), "Test About")


class AboutViewTest(TestCase):
    """Test the About page view"""

    def test_about_page_with_content(self):
        """Test About page displays content when it exists"""
        About.objects.create(
            title="Test About",
            content="Test content"
        )
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test About")
        self.assertContains(response, "Test content")

    def test_about_page_without_content(self):
        """Test About page displays message when no content exists"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No content available yet")


class AboutAdminTest(TestCase):
    """Test the About admin interface"""

    def test_about_admin_registered(self):
        """Test that About model is registered in admin"""
        from django.contrib import admin
        from .models import About
        self.assertIn(About, admin.site._registry)
