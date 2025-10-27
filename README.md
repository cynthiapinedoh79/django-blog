# Django Blog with Comments

A Django blog application that allows users to leave comments on posts and engage in threaded conversations.

## Features

- **Blog Posts**: Create and view blog posts
- **Comment System**: Users can leave comments on posts
- **Comment Approval**: Comments require admin approval before being displayed (AC1)
- **Reply Functionality**: Users can reply to comments (AC2)
- **Threaded Conversations**: Comments and replies create conversation threads (AC3)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `http://localhost:8000/admin/` to:
   - Create blog posts
   - Approve comments
   - Manage users

2. View blog posts at `http://localhost:8000/`

3. Click on a post to view details and leave comments

## Models

### Post
- Title, slug, author, content
- Status (Draft/Published)
- Timestamps

### Comment
- Post reference
- Author reference
- Body text
- Approved status (for moderation)
- Parent comment (for threading/replies)
- Timestamps

## Testing

The test credentials created for development:
- Admin: username `admin`, password `admin123`
- Test User: username `testuser`, password `test123`
