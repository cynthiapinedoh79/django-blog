# Django Blog

A Django blog application with draft post functionality.

## Features

- Create and manage blog posts
- Draft and Published post statuses
- Admin interface for content management
- Filter posts by status (Draft/Published)
- Auto-slug generation from titles

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cynthiapinedoh79/django-blog.git
cd django-blog
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (optional):
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the admin interface at http://localhost:8000/admin/

## Usage

### Creating Draft Posts

1. Log in to the admin interface
2. Navigate to Blog → Posts → Add post
3. Fill in the post details
4. Keep the Status as "Draft" (default)
5. Click "Save"

### Finishing Draft Posts Later

1. Log in to the admin interface
2. Navigate to Blog → Posts
3. Click on the draft post you want to edit
4. Update the content
5. Click "Save" to keep as draft, or change Status to "Published" and save

## Running Tests

```bash
python manage.py test blog
```

## Project Structure

- `blog/` - Blog application
  - `models.py` - Post model with draft/published status
  - `admin.py` - Admin interface configuration
  - `tests.py` - Test suite for draft functionality
- `codestar/` - Django project settings
- `manage.py` - Django management script

## License

MIT License
