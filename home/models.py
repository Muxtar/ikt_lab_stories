from ast import arg
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# import sqlite3

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    subjets = models.IntegerField(choices=((1, 'Teklif'), (2, 'Irad')))
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.username} {self.message[:10]}..."

class Tag(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=30, )
    picture = models.ImageField(upload_to='category/')
    slug = models.SlugField(blank = True, null = True)

    def save(self, *args, **kwargs):
        self.slug =  slugify(f'{self.name}-{self.id}')#''.join(self.name.split())
        super().save(args, kwargs)

    def __str__(self) -> str:
        return self.name

class Stories(models.Model):
    category_id = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='stories')
    cover_image = models.ImageField(upload_to = 'stories/cover/')
    back_image = models.ImageField(upload_to = 'stories/back/')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title

    def save(self,*args, **kwargs):
        return super().save(*args, **kwargs)

