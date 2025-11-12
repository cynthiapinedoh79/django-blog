# Django Blog

A simple Django blog application that allows users to view blog posts.

## Features

- List view of all published blog posts
- Detailed view for individual blog posts (click on a post to read full text)
- Admin interface for managing blog posts
- Support for draft and published posts
- Author and date information for each post

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/ to see the blog

## Usage

### As a Site User
- Browse the list of published blog posts on the home page
- Click on any post title to view the full content of that post
- Use the "Back to all posts" link to return to the list view

### As an Admin
- Access the admin panel at http://127.0.0.1:8000/admin/
- Create, edit, and manage blog posts
- Set posts as Draft or Published
- Manage authors and other content

## Testing

Run the test suite:
```bash
python manage.py test blog
```

## User Story Implementation

**As a Site User, I can click on a post so that I can read the full text**

**Acceptance Criteria:**
- ✅ AC1: When a blog post title is clicked on a detailed view of the post is seen.

The implementation includes:
- A `PostDetail` view that displays the full content of a blog post
- URL routing that maps post slugs to the detail view
- A template that shows the complete post content, author, and dates
- Clickable links on the post list page that navigate to the detail view
- Tests that verify the functionality works as expected
