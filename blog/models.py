from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_requires = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return '{}-{}'.format(self.title, self.id)
    
    def get_excerpt(self):
        """خلاصه متن بدون HTML"""
        text = strip_tags(self.content)
        words = text.split()
        if len(words) > 20:
            return ' '.join(words[:20]) + '...'
        return text
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
  



class NewsletterEmail(models.Model):
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email