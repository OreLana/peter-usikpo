from django.contrib import admin
from pugapi.models.user import User
from pugapi.models.category import Category
from pugapi.models.event import Event
from pugapi.models.newsletter import Newsletter
from pugapi.models.article import Article

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Newsletter)
admin.site.register(Article)