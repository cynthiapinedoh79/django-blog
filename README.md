# Django Blog

A simple Django blog application with user registration and commenting features.

## Features

- User registration with email
- User login/logout
- View blog posts
- Authenticated users can comment on posts
- Admin panel for managing posts and comments

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the application at http://localhost:8000/

## Usage

### User Registration and Login

1. Navigate to the home page
2. Click "Register" in the navigation bar
3. Enter your email and password
4. After registration, you can log in with your credentials

### Commenting on Posts

1. Register and log in to your account
2. Navigate to a blog post
3. Scroll to the comments section
4. Enter your comment and click "Submit"
5. Your comment will be submitted for approval by an administrator

### Admin Panel

1. Log in to the admin panel at http://localhost:8000/admin/
2. Use the superuser credentials you created
3. You can:
   - Create, edit, and delete blog posts
   - Approve or reject comments
   - Manage users

## Running Tests

Run the test suite:
```bash
python manage.py test
```

## Acceptance Criteria

✅ **AC1**: Given an email, a user can register an account  
✅ **AC2**: Then the user can log in  
✅ **AC3**: When the user is logged in, they can comment

## Project Structure

```
django-blog/
├── blog/               # Blog application
│   ├── models.py      # Post and Comment models
│   ├── views.py       # Views for posts and comments
│   ├── forms.py       # Comment form
│   ├── admin.py       # Admin configuration
│   └── tests.py       # Test suite
├── config/            # Project configuration
│   ├── settings.py    # Django settings
│   └── urls.py        # URL configuration
├── templates/         # HTML templates
│   ├── base.html      # Base template
│   └── blog/          # Blog templates
└── requirements.txt   # Python dependencies
```

## Technologies Used

- Django 5.2.7
- django-allauth 65.12.1 (for user authentication)
- Bootstrap 5.1.3 (for styling)
- SQLite (database)
