from django.test import TestCase
from django.contrib.admin.sites import site
from .models import About
from .admin import AboutAdmin


class AboutModelTest(TestCase):
    """
    Test cases for About model.
    """

    def test_about_model_creation(self):
        """Test that About model can be created."""
        about = About.objects.create(
            title="About Us",
            content="This is the about page content."
        )
        self.assertEqual(about.title, "About Us")
        self.assertEqual(about.content, "This is the about page content.")
        self.assertIsNotNone(about.updated_on)

    def test_about_str_method(self):
        """Test the __str__ method of About model."""
        about = About.objects.create(
            title="Test Title",
            content="Test content"
        )
        self.assertEqual(str(about), "Test Title")


class AboutAdminTest(TestCase):
    """
    Test cases for About admin registration.
    """

    def test_about_is_registered_in_admin(self):
        """Test that About model is registered in admin panel."""
        self.assertIn(About, site._registry)
        self.assertIsInstance(site._registry[About], AboutAdmin)

    def test_about_admin_list_display(self):
        """Test that admin list display is configured correctly."""
        admin_instance = AboutAdmin(About, site)
        self.assertEqual(admin_instance.list_display, ('title', 'updated_on'))

    def test_about_admin_search_fields(self):
        """Test that admin search fields are configured correctly."""
        admin_instance = AboutAdmin(About, site)
        self.assertEqual(admin_instance.search_fields, ['title', 'content'])
