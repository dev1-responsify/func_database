from django.db import models

class Metrics(models.Model):
    website = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    blog_date = models.DateTimeField('date published')
    blog_url= models.CharField(max_length=200)
    word_count = models.IntegerField(default=0)
    image_count = models.IntegerField(default=0)
    header_one =  models.CharField(max_length=200)
    header_two =  models.CharField(max_length=200)
    header_three =  models.CharField(max_length=200)
    #links outside the blog
    external_link = models.CharField(max_length=200)
    #internal matches domain of site
    internal_link = models.CharField(max_length=200)
    readability_score = models.IntegerField(default=0)
    #self promotional score
    company_name = models.IntegerField(default=0)
