# Django Blog

A Django blog application with comment approval functionality.

## Features

- Blog posts with comments
- Comment approval/disapproval system for site admins
- Admin interface for managing posts and comments
- User authentication

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

6. Access the admin interface at: http://127.0.0.1:8000/admin/

## Comment Approval Feature

### Acceptance Criteria

**AC1**: Given a logged in user, they can approve a comment
**AC2**: Given a logged in user, they can disapprove a comment

### Usage

#### Via Admin Interface

1. Log in to the Django admin interface
2. Navigate to the Comments section
3. Select one or more comments
4. Choose "Approve selected comments" or "Disapprove selected comments" from the actions dropdown
5. Click "Go"

#### Via URL Endpoints

Logged-in users can also approve/disapprove comments via URL endpoints:

- Approve: `/blog/comment/<comment_id>/approve/`
- Disapprove: `/blog/comment/<comment_id>/disapprove/`

### Models

#### Post
- `title`: Post title
- `content`: Post content
- `author`: Foreign key to User
- `created_at`: Auto-generated timestamp
- `updated_at`: Auto-updated timestamp

#### Comment
- `post`: Foreign key to Post
- `author`: Foreign key to User
- `content`: Comment content
- `created_at`: Auto-generated timestamp
- `approved`: Boolean field (default: False) - determines if comment is approved

## Running Tests

```bash
python manage.py test blog
```

All tests validate the comment approval functionality including:
- Comments created unapproved by default
- Authentication required for approval/disapproval
- Approval functionality (AC1)
- Disapproval functionality (AC2)
- Bulk approve/disapprove operations

## License

MIT
