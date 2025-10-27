# Django Blog

A simple blog application built with Django that allows users to view and read blog posts.

## Features

- View a list of published blog posts
- Click on a post title to view the full post content
- Responsive design with clean UI
- Admin interface for managing posts
- Author information and timestamps displayed

## Installation

1. Clone the repository
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

6. Access the application at http://localhost:8000/

## Usage

### Viewing Posts

- Navigate to the home page to see a list of published blog posts
- Click on any post title or "Read More" link to view the full post
- Use the "Back to Blog" button to return to the post list

### Managing Posts

- Access the admin interface at http://localhost:8000/admin/
- Log in with your superuser credentials
- Add, edit, or delete blog posts
- Set post status to Published (1) to make it visible on the site

## Running Tests

```bash
python manage.py test blog
```

## Project Structure

- `blog/` - Main blog application
  - `models.py` - Post model definition
  - `views.py` - List and detail views for posts
  - `urls.py` - URL routing for blog app
  - `admin.py` - Admin configuration
  - `tests.py` - Test cases
  - `templates/blog/` - HTML templates
- `codestar/` - Django project settings
