# Django Blog

A Django blog application with an About page that can be managed through the admin panel.

## Features

- About page content management through Django admin
- Site administrators can create and update About page content
- Simple, clean interface

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

6. Access the admin panel at `http://localhost:8000/admin/`
7. Access the About page at `http://localhost:8000/about/`

## Admin Panel

Site administrators can manage the About page content through the Django admin panel:

1. Log in to the admin panel
2. Navigate to the "About" section
3. Add or edit About page content
4. Save changes

The About page will automatically display the updated content.
