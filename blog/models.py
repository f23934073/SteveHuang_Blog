from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model): 
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model): 
    title = models.CharField(max_length=70)#文章標題
    body = models.TextField()#內文
    excerpt = models.CharField(max_length=200, blank=True)#摘要
    created_time = models.DateTimeField()#創建時間
    modified_time = models.DateTimeField()#更新時間
    category = models.ForeignKey(Category)#類別
    tags = models.ManyToManyField(Tag, blank=True)#標籤
    author = models.ForeignKey(User)#作者
    views = models.PositiveIntegerField(default=0, editable=False)
    def get_absolute_url(self): 
        return reverse('blog:detail', kwargs={'pk': self.pk})
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

class UpFile(models.Model):
    up_file = models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.up_file