# Django Blog

A simple Django blog application with comment functionality, including the ability for users to modify and delete their own comments.

## Features

- View blog posts
- User authentication (login/logout)
- Add comments to blog posts
- **Edit your own comments**
- **Delete your own comments**
- Admin interface for managing posts and comments

## Requirements

- Python 3.12+
- Django 5.2.7

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

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://localhost:8000 in your browser

## Test Users

The following test users are available:
- Username: `testuser1`, Password: `testpass123`
- Username: `testuser2`, Password: `testpass123`
- Admin: `admin`, Password: `admin123`

## Usage

### Viewing Posts
- Navigate to the home page to see all published blog posts
- Click on a post title to view the full post and its comments

### Commenting
- You must be logged in to add comments
- On a post detail page, use the comment form at the bottom to add your comment

### Editing Comments
- Only the comment author can edit their comments
- Click the "Edit" button next to your comment
- Modify the comment text and click "Save Changes"

### Deleting Comments
- Only the comment author can delete their comments
- Click the "Delete" button next to your comment
- Confirm the deletion on the confirmation page

## Admin Interface

Access the admin interface at http://localhost:8000/admin/ to:
- Create, edit, and delete blog posts
- Manage comments
- Manage users

## Project Structure

```
django-blog/
├── blog/                   # Main blog application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── blog/          # Blog-specific templates
│   │   └── registration/  # Authentication templates
│   ├── admin.py           # Admin interface configuration
│   ├── forms.py           # Comment form
│   ├── models.py          # Post and Comment models
│   ├── urls.py            # Blog URL patterns
│   └── views.py           # View functions
├── blogproject/           # Project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL patterns
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## License

This project is open source and available under the MIT License.
