from django.db import models
from pugapi.models.user import User
from pugapi.models.category import Category
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField('Category', related_name='article')
    content = RichTextUploadingField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)