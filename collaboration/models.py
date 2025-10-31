from django.db import models

# Create your models here.

class CollaborationRequest(models.Model):
    """Model to store collaboration requests from potential collaborators."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.email}"

