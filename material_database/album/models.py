from django.db import models



class Image(models.Model):
    picture = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.picture.url
# Create your models here.

