# Django Blog

A simple Django blog application with draft post functionality.

## Features

- **Draft Posts**: Site admins can create draft blog posts that are not visible to the public
- **Published Posts**: Posts can be published to make them visible to all visitors
- **Admin Interface**: Full Django admin interface for managing posts
- **Post Management**: Create, edit, and manage blog posts with title, content, and status

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

### Creating Draft Posts

1. Access the admin interface at `http://localhost:8000/admin/`
2. Log in with your superuser credentials
3. Navigate to "Posts" and click "Add Post"
4. Fill in the post details:
   - Title: The post title
   - Slug: URL-friendly version of the title (auto-populated)
   - Content: The post content
   - Status: Select "Draft" to save as draft
5. Click "Save" to create the draft post

### Publishing Draft Posts

1. In the admin interface, go to the post list
2. Click on the draft post you want to publish
3. Change the Status from "Draft" to "Published"
4. Click "Save"
5. The post will now be visible on the public blog

### Viewing Posts

- **Public blog**: Visit `http://localhost:8000/` to see all published posts
- **Individual post**: Click on any post title to view its full content
- **Draft posts**: Only visible in the admin interface, not accessible to the public

## Acceptance Criteria

✅ **AC1**: Given a logged in user, they can save a draft blog post
- Admin users can create posts with status="draft" through the Django admin interface

✅ **AC2**: Then they can finish the content later
- Draft posts are saved in the database and can be edited at any time
- Drafts remain in draft status until explicitly changed to "published"
- Drafts are not visible to public visitors

## Testing

Run the test suite:
```bash
python manage.py test
```

The tests verify:
- Draft posts can be created
- Published posts can be created
- Default status is "draft"
- Only published posts appear in public views
- Draft posts return 404 when accessed directly
- Published posts are accessible via their detail URLs

## Models

### Post

- `title`: CharField (max 200 characters)
- `slug`: SlugField (unique, URL-friendly)
- `author`: ForeignKey to User
- `content`: TextField
- `created_on`: DateTimeField (auto-generated)
- `updated_on`: DateTimeField (auto-updated)
- `status`: CharField with choices ('draft', 'published'), defaults to 'draft'

## Views

- **PostListView**: Displays all published posts (paginated, 6 per page)
- **PostDetailView**: Displays a single published post

## Admin Features

- List display shows: title, slug, status, author, created_on
- Filtering by status, created date, and author
- Search by title and content
- Auto-populated slug field based on title
- Date hierarchy navigation
- Automatic author assignment on post creation
