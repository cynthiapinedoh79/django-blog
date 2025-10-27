# Django Blog

A simple Django blog application that allows authenticated users to manage blog posts with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- **Create Posts**: Logged-in users can create new blog posts
- **Read Posts**: All users can view blog posts
- **Update Posts**: Logged-in users can edit existing posts
- **Delete Posts**: Logged-in users can delete posts
- **Admin Interface**: Full admin interface for post management
- **Authentication**: Login required for create, update, and delete operations

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

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application:
- Blog: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Usage

### Admin Interface
Log in to the admin interface at `/admin/` to manage posts with full CRUD capabilities.

### Web Interface
- **View Posts**: Visit the home page to see all blog posts
- **Create Post**: Click "Create Post" (requires login)
- **Edit Post**: Click "Edit" on any post detail page (requires login)
- **Delete Post**: Click "Delete" on any post detail page (requires login)

## Running Tests

```bash
python manage.py test blog
```

## Acceptance Criteria

✅ **AC1**: Given a logged in user, they can create a blog post  
✅ **AC2**: Given a logged in user, they can read a blog post  
✅ **AC3**: Given a logged in user, they can update a blog post  
✅ **AC4**: Given a logged in user, they can delete a blog post  

## Project Structure

```
django-blog/
├── blog/                   # Blog application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py          # Admin interface configuration
│   ├── models.py         # Post model
│   ├── views.py          # View functions
│   ├── urls.py           # URL patterns
│   └── tests.py          # Test cases
├── blogproject/           # Project settings
│   ├── settings.py       # Django settings
│   └── urls.py           # Main URL configuration
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Technologies

- Python 3.12+
- Django 5.2+
- SQLite (default database)
