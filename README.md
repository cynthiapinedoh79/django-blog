# Django Blog with Comment Approval

A Django blog application that allows site administrators to approve or disapprove comments.

## Features

- Blog posts with author and timestamps
- Comments on posts with approval system
- Admin interface for managing posts and comments
- Bulk approval/disapproval actions for comments

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Access the admin interface at http://127.0.0.1:8000/admin/

## Comment Approval Functionality

### Acceptance Criteria

**AC1**: Given a logged in user, they can approve a comment
- Admin users can log into the Django admin interface
- In the Comments section, admins can select one or more comments
- Using the "Approve selected comments" action, they can approve comments
- Alternatively, they can edit individual comments and set the "approved" field to True

**AC2**: Given a logged in user, they can disapprove a comment
- Admin users can log into the Django admin interface
- In the Comments section, admins can select one or more comments
- Using the "Disapprove selected comments" action, they can disapprove comments
- Alternatively, they can edit individual comments and set the "approved" field to False

### Models

#### Post
- `title`: Post title
- `content`: Post content
- `author`: Author (ForeignKey to User)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

#### Comment
- `post`: Associated post (ForeignKey to Post)
- `author`: Comment author (ForeignKey to User)
- `content`: Comment content
- `created_at`: Creation timestamp
- `approved`: Boolean field indicating approval status (default: False)

### Admin Interface

The admin interface provides:
- List view showing comment author, post, creation time, and approval status
- Filtering by approval status and creation date
- Search by comment content and author username
- Bulk actions to approve or disapprove multiple comments at once
- Individual comment editing with approval checkbox

## Running Tests

Run the test suite:
```bash
python manage.py test blog
```

## Security

- Only authenticated admin users can access the comment approval functionality
- All comment operations are protected by Django's built-in admin authentication
- Comments are unapproved by default to filter out objectionable content
