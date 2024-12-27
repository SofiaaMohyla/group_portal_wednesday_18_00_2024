from django.contrib import admin

from forum.models import Forum, Comment

admin.site.register(Comment)
admin.site.register(Forum)
# Register your models here.
