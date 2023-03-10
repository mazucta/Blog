from django.db import models
from django.shortcuts import reverse 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250,db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag',blank=True,related_name='posts')
    image = models.ImageField(upload_to='images/', default='images/default.jpg' )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug} )

    class Meta:
        ordering = ['-pk']



class Tag(models.Model):
    title = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=50,unique=True)
    

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('tag_detail_url',kwargs={'pk':self.pk} )

    


