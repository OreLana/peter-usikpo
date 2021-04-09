from django.db import models
from pugapi.models.user import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Newsletter(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)