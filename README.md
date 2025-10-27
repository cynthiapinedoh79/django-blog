# Django Blog

A simple blog application built with Django that allows users to register accounts, log in, and comment on blog posts.

## Features

- User registration with email validation
- User authentication (login/logout)
- Blog post listing and detail views
- Commenting system (requires authentication)
- Admin interface for managing posts and comments
- Responsive Bootstrap 5 design

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

6. Visit http://localhost:8000 to view the blog

## Usage

### For Site Users:
1. Register for an account at `/accounts/register/`
2. Log in at `/accounts/login/`
3. Browse blog posts on the homepage
4. Click "Read More" to view a post detail
5. Add comments when logged in

### For Administrators:
1. Access the admin panel at `/admin/`
2. Create and manage blog posts
3. Moderate comments
4. Manage users

## Project Structure

```
django-blog/
├── accounts/          # User authentication app
├── blog/              # Blog posts and comments app
├── config/            # Project settings
├── templates/         # HTML templates
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## Technologies Used

- Django 4.2.25
- Python 3.12
- Bootstrap 5
- Django Crispy Forms
- SQLite (development database)

## License

This project is open source and available for educational purposes.
