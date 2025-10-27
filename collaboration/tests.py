from django.test import TestCase, Client
from django.urls import reverse
from .models import CollaborationRequest
from .forms import CollaborationForm

# Create your tests here.

class CollaborationRequestModelTest(TestCase):
    """Test the CollaborationRequest model."""
    
    def test_create_collaboration_request(self):
        """Test creating a collaboration request."""
        request = CollaborationRequest.objects.create(
            name="John Doe",
            email="john@example.com",
            website="https://johndoe.com",
            message="I'd like to collaborate on a project."
        )
        self.assertEqual(request.name, "John Doe")
        self.assertEqual(request.email, "john@example.com")
        self.assertEqual(str(request), "John Doe - john@example.com")
    
    def test_collaboration_request_without_website(self):
        """Test creating a collaboration request without website (optional field)."""
        request = CollaborationRequest.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            message="Looking forward to working together."
        )
        self.assertIsNone(request.website)


class CollaborationFormTest(TestCase):
    """Test the CollaborationForm."""
    
    def test_form_valid_with_all_fields(self):
        """Test form is valid with all fields filled (AC1)."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'website': 'https://johndoe.com',
            'message': 'I would like to collaborate on your project.'
        }
        form = CollaborationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_form_valid_without_website(self):
        """Test form is valid without website (optional field) (AC1)."""
        form_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'message': 'Looking forward to collaborating.'
        }
        form = CollaborationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_form_invalid_without_name(self):
        """Test form is invalid without name (required field) (AC3)."""
        form_data = {
            'email': 'john@example.com',
            'message': 'Test message'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
    
    def test_form_invalid_without_email(self):
        """Test form is invalid without email (required field) (AC3)."""
        form_data = {
            'name': 'John Doe',
            'message': 'Test message'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_form_invalid_with_bad_email(self):
        """Test form is invalid with bad email format (AC3)."""
        form_data = {
            'name': 'John Doe',
            'email': 'not-an-email',
            'message': 'Test message'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_form_invalid_without_message(self):
        """Test form is invalid without message (required field) (AC3)."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com'
        }
        form = CollaborationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)


class CollaborationViewTest(TestCase):
    """Test the collaboration view."""
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('collaboration:request')
    
    def test_get_collaboration_form(self):
        """Test GET request displays the form."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Collaboration Request')
        self.assertIsInstance(response.context['form'], CollaborationForm)
    
    def test_post_valid_form(self):
        """Test POST with valid data creates request and shows success message (AC2)."""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'website': 'https://johndoe.com',
            'message': 'I would like to collaborate.'
        }
        response = self.client.post(self.url, data=form_data)
        
        # Check redirect
        self.assertEqual(response.status_code, 302)
        
        # Check that the collaboration request was created (AC4)
        self.assertEqual(CollaborationRequest.objects.count(), 1)
        request = CollaborationRequest.objects.first()
        self.assertEqual(request.name, 'John Doe')
        self.assertEqual(request.email, 'john@example.com')
        
        # Follow redirect and check for success message (AC2)
        response = self.client.get(self.url)
        self.assertContains(response, 'proposal has been sent successfully')
    
    def test_post_invalid_form_missing_required_field(self):
        """Test POST with missing required field shows error (AC3)."""
        form_data = {
            'name': 'John Doe',
            # Missing email (required)
            'message': 'Test message'
        }
        response = self.client.post(self.url, data=form_data)
        
        # Should not redirect
        self.assertEqual(response.status_code, 200)
        
        # No collaboration request should be created
        self.assertEqual(CollaborationRequest.objects.count(), 0)
        
        # Should show error message
        self.assertContains(response, 'Please correct the errors')
    
    def test_post_invalid_form_bad_email(self):
        """Test POST with invalid email format shows error (AC3)."""
        form_data = {
            'name': 'John Doe',
            'email': 'not-a-valid-email',
            'message': 'Test message'
        }
        response = self.client.post(self.url, data=form_data)
        
        # Should not redirect
        self.assertEqual(response.status_code, 200)
        
        # No collaboration request should be created
        self.assertEqual(CollaborationRequest.objects.count(), 0)
        
        # Should show email validation error
        self.assertContains(response, 'valid email')

