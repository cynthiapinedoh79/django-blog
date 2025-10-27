# Django Blog

A simple Django blog application with paginated post listings.

## Features

- View paginated list of blog posts
- Admin interface for managing posts
- Responsive design with card-based layout
- 6 posts per page with navigation controls

## Installation

1. Install dependencies:
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

5. Access the blog at http://localhost:8000/

## Admin Access

Access the admin interface at http://localhost:8000/admin/ to manage blog posts.

## Project Structure

- `blog/` - Main blog application
  - `models.py` - Post model definition
  - `views.py` - PostList view with pagination
  - `templates/blog/` - HTML templates
- `codestar/` - Project settings and configuration
