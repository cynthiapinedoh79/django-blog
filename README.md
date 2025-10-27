# Django Blog with Comments

A Django blog application with comment functionality that supports user comments, comment approval, and threaded replies.

## Features

- **Blog Posts**: Create and view blog posts
- **Comments**: Users can leave comments on posts
- **Comment Approval**: Comments require admin approval before being displayed (AC1)
- **Reply Functionality**: Users can reply to comments (AC2)
- **Conversation Threading**: Multiple comments create threaded conversations (AC3)
- **Admin Interface**: Manage posts and approve/disapprove comments

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

5. Access the admin panel at http://localhost:8000/admin to create posts and manage comments

## Usage

### Creating Blog Posts
- Log in to the admin panel
- Create a new Post with title, content, and set status to "Published"

### Commenting
- Users must be logged in to comment
- Comments are submitted for approval
- Once approved, comments appear on the post
- Users can reply to existing approved comments

### Managing Comments
- Admin users can approve/disapprove comments from the admin panel
- Bulk actions are available for approving multiple comments at once

## Models

### Post
- Title, slug, author, content
- Created/updated timestamps
- Status (Draft/Published)

### Comment
- Related to a Post
- Author, content, created timestamp
- Approval status (approved/not approved)
- Parent comment (for threading/replies)
