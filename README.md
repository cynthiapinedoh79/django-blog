# Django Blog

A simple Django blog application with an About page.

## Features

- Home page
- About page with site information
- Navigation menu with Home and About links

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

4. Start the development server:
```bash
python manage.py runserver
```

5. Visit http://localhost:8000/ in your browser

## Testing

Run the test suite:
```bash
python manage.py test
```

## Project Structure

- `codestar/` - Main Django project configuration
- `blog/` - Blog app with home page
- `about/` - About app with about page
- `templates/` - HTML templates

## Security Note

**Important**: The SECRET_KEY in `settings.py` is for development only. For production deployment:
1. Generate a new SECRET_KEY
2. Store it in an environment variable
3. Never commit production secrets to version control
