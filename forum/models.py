from django.db import models
from django.conf import settings

# Create your models here.

class Forum(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forums')
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return self.task.get_absolute_url()