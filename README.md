# Django Blog - Collaboration Request Feature

A Django-based blog application with a collaboration request form for potential collaborators to submit partnership proposals.

## Features

- **Collaboration Request Form**: Allows potential collaborators to submit their information and collaboration proposals
- **Form Validation**: Validates required fields (Name, Email, Message) and email format
- **Success Confirmation**: Displays on-screen success message after successful submission
- **Email Notifications**: Sends email notifications to the site owner with collaboration details
- **Admin Interface**: Manage collaboration requests through Django admin panel

## Requirements

- Python 3.8+
- Django 5.2+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cynthiapinedoh79/django-blog.git
cd django-blog
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) For production, copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
# Edit .env with your production settings
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the collaboration form at: http://localhost:8000/collaborate/

## Running Tests

```bash
python manage.py test collaboration
```

## Form Fields

- **Name** (Required): Collaborator's full name
- **Email** (Required): Valid email address
- **Website/Portfolio URL** (Optional): Link to collaborator's website or portfolio
- **Message/Proposal** (Required): Description of the collaboration proposal

## Email Configuration

By default, the application uses Django's console email backend for development. To configure production email settings, update the following in `blog_project/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## Project Structure

```
django-blog/
├── blog_project/          # Main project configuration
│   ├── settings.py        # Project settings
│   └── urls.py            # URL routing
├── collaboration/         # Collaboration app
│   ├── models.py          # CollaborationRequest model
│   ├── forms.py           # CollaborationForm
│   ├── views.py           # Form view and submission logic
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin configuration
│   ├── tests.py           # Test suite
│   └── templates/         # HTML templates
│       └── collaboration/
│           └── request_form.html
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## License

This project is open source and available under the MIT License.
