from django.db import models
# Create your models here.

class Post(models.Model):

    PENDING = 0
    ACCEPTED = 1
    NOT_NOW =2
    REJECTED = 3

    STATUS = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (NOT_NOW, 'NOT_NOW'),
        (REJECTED, 'Rejected')
    )

    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photo_album")
    pub_date = models.DateTimeField('date published', auto_now=True)
    rating = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUS , default=0)

    def __unicode__(self):
        return self.photo

   #modeluj opstine kao konstante?
    # street = models.CharField(max_length=200)
    # county = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
