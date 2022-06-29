from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The post model
class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

# The comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content
