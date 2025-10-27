from django.test import TestCase
from django.urls import reverse


class AboutPageTestCase(TestCase):
    """Test case for the About page"""

    def test_about_page_status_code(self):
        """Test that the about page returns a 200 status code"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_uses_correct_template(self):
        """Test that the about page uses the correct template"""
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_about_page_contains_about_text(self):
        """Test that the about page contains the about text"""
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About')
        self.assertContains(response, 'Welcome to our Django Blog')

    def test_about_link_in_navigation(self):
        """Test that the About link is present in the navigation"""
        response = self.client.get(reverse('home'))
        about_url = reverse('about')
        self.assertContains(response, f'href="{about_url}"')
        self.assertContains(response, '>About<')
