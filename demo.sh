#!/bin/bash

# Demonstration script for draft post functionality

# Cleanup function to ensure server is stopped
cleanup() {
    if [ ! -z "$SERVER_PID" ]; then
        kill $SERVER_PID 2>/dev/null
        wait $SERVER_PID 2>/dev/null
    fi
}

# Set trap to cleanup on exit
trap cleanup EXIT INT TERM

echo "=== Django Blog Draft Post Functionality Demo ==="
echo ""

# Check if database exists
if [ ! -f db.sqlite3 ]; then
    echo "Database not found. Please run:"
    echo "  python manage.py migrate"
    echo "  python manage.py createsuperuser"
    exit 1
fi

echo "1. Creating sample posts..."
python manage.py shell << 'EOF'
from django.contrib.auth.models import User
from blog.models import Post

# Get or create admin user
admin = User.objects.first()
if not admin:
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

# Clear existing posts for demo
Post.objects.all().delete()

# Create draft posts
Post.objects.create(
    title='Draft: Future Blog Post',
    slug='draft-future-blog-post',
    author=admin,
    content='This is a draft that I will finish later.',
    status='draft'
)

# Create published post
Post.objects.create(
    title='Published: Welcome Post',
    slug='published-welcome-post',
    author=admin,
    content='This is a published post visible to everyone.',
    status='published'
)

print("✓ Created 1 draft post and 1 published post")
EOF

echo ""
echo "2. Checking database:"
python manage.py shell << 'EOF'
from blog.models import Post

total = Post.objects.count()
draft_count = Post.objects.filter(status='draft').count()
published_count = Post.objects.filter(status='published').count()

print(f"  Total posts: {total}")
print(f"  Draft posts: {draft_count}")
print(f"  Published posts: {published_count}")
EOF

echo ""
echo "3. Testing public visibility:"
python manage.py runserver 127.0.0.1:8000 > /tmp/server.log 2>&1 &
SERVER_PID=$!
sleep 2

echo "  - Fetching public blog page..."
RESPONSE=$(curl -s http://localhost:8000/)
if echo "$RESPONSE" | grep -q "Published: Welcome Post"; then
    echo "    ✓ Published post is visible"
else
    echo "    ✗ Published post NOT visible"
fi

if echo "$RESPONSE" | grep -q "Draft: Future Blog Post"; then
    echo "    ✗ Draft post is incorrectly visible"
else
    echo "    ✓ Draft post is NOT visible (correct)"
fi

echo "  - Testing direct access to draft post..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/post/draft-future-blog-post/)
if [ "$STATUS" == "404" ]; then
    echo "    ✓ Draft post returns 404 (correct)"
else
    echo "    ✗ Draft post returns $STATUS (should be 404)"
fi

echo "  - Testing direct access to published post..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/post/published-welcome-post/)
if [ "$STATUS" == "200" ]; then
    echo "    ✓ Published post returns 200 (correct)"
else
    echo "    ✗ Published post returns $STATUS (should be 200)"
fi

echo ""
echo "=== Demo Complete ==="
echo ""
echo "To access the admin interface:"
echo "  1. Start server: python manage.py runserver"
echo "  2. Visit: http://localhost:8000/admin/"
echo "  3. Login with admin credentials"
echo "  4. Navigate to Posts to manage draft/published posts"
