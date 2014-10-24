from django.db import models
# Create your models here.

class Post(models.Model):
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photo_album")
    pub_date = models.DateTimeField('date published', auto_now=True)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.photo

   #modeluj opstine kao konstante?
    # street = models.CharField(max_length=200)
    # county = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
