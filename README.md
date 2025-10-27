# Django Blog

A simple Django blog application that allows users to view blog posts and read comments.

## Features

- View list of published blog posts
- View individual blog posts with detailed content
- View comments on each post
- Admin interface for managing posts and comments
- Comment approval system for moderating user comments

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run database migrations:
```bash
python manage.py migrate
```

3. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the application:
   - Blog: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Usage

### For Site Users
- Browse the list of blog posts on the home page
- Click on any post title to view the full post and read comments
- Approved comments are displayed in chronological order

### For Admins
- Log in to the admin interface at `/admin/`
- View all comments under Blog > Comments
- Filter comments by approval status
- Use bulk actions to approve multiple comments at once
- View which post each comment belongs to

## Models

### Post
- Title, slug, author, content
- Creation and update timestamps
- Status (Draft/Published)

### Comment
- Associated post, author name, email
- Comment body
- Creation timestamp
- Approval status

## Admin Features

The admin interface provides:
- List view of all comments with filtering options
- Ability to approve/disapprove comments
- Search functionality
- Comments organized by post
