from django.db import models
from accounts.models import User

class Categories(models.Model):
    CATEGORY_CHOICES=(
        ('politics','Politics'),
        ('business','Business'),
        ('sports','Sports'),
        ('agriculture','Agriculture'),
        ('fashion','Fashion')
    )
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.category}"

class Post(models.Model):
    title=models.CharField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="categories")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} about {self.post}"