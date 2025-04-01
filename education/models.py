
from django.db import models
from users.models import User

class EducationalContent(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    file_url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)