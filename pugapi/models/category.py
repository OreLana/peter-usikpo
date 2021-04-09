from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)