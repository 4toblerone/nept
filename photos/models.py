#coding: utf-8
from django.db import models
from PIL import Image
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import StringIO
from operator import itemgetter

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

    MUNICIPALITY = ['Barajevo', 'Vozdovac', 'Vracar', 'Grocka', 'Zvezdara',
               'Zemun', 'Lazarevac', 'Mladenovac', 'Novi Beograd',
               'Obrenovac', 'Palilula', 'Rakovica', 'Savski venac',
               'Sopot', 'Stari grad', 'Surcin', 'Cukarica' ]
    # MUNICIPALITY = (('Barajevo','Barajevo'),
    #                 ('Vozdovac', 'Vozdovac'),
    #                 ('Vracar','Vracar')
    # )
    description = models.CharField(max_length=200)
    #resize?
    #should i create separate field thumbnail? YES, y d fuck not
    #also create field for original photos
    photo = models.ImageField(upload_to="photo_album")
    original_photo = models.ImageField(upload_to="photo_album/originals", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="photo_album/thumbnails", null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now=True)
    rating = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUS , default=ACCEPTED)
    city_part = models.CharField(choices=((x,x) for x in MUNICIPALITY),
                                 default = 'NEPOZNATO', max_length="51")

    def admin_thumbnail(self):
        # think about thumbnail size
        return u'<img src="{url}" width="200" height="150" />'.format(url=self.thumbnail.url)
    admin_thumbnail.short_description = "Thumbnail"
    admin_thumbnail.allow_tags = True

     #override Model save method with custom one
    #which will create thumbnail before saving post
    #should i use external lib (eg. sorl) for it?

    def resize(self, photo,max_side):
        """
        Resizes photo so that longer side of the photo will
        be max_side and shorter one will be calculated based
        on the proportion of longer side and max_side
        """
        w, h = photo.size
        #if photo is in la
        if w>h:
            min_side = w/max_side*h
            photo.thumbnail((max_side,min_side), Image.ANTIALIAS)
            return photo
        else:
            print  "usao u else"
            min_side = h/max_side*w
            photo.thumbnail((min_side,max_side), Image.ANTIALIAS)
            return photo

    def _save(self,img_field, max_side, img, photo_name):
        io = StringIO.StringIO()
        resized = self.resize(img,max_side)
        resized.save(io, format = resized.format)
        img_field.save(photo_name, ContentFile(io.getvalue()), save = False)
        pass

    def save(self):
        #from larger to smaller
        img = Image.open(self.original_photo.file)
        self._save(self.photo, 650, img, self.original_photo.name)
        self._save(self.thumbnail, 200, img, self.original_photo.name)
        super(Post, self).save()

    def __unicode__(self):
        return self.description

# put names of city parts in a separate constants file
# Djurinci
# Jabučki Rit
# Jagnjilo (Mladenovac)
# Jakovo
# Jajinci
# Ada Međica
# Altina
# Amerić
# Arnajevo
# Babe (Sopot)
# Batajnica
# Banjica
# Baćevac
# Begaljica
# Bežanija
# Bežanijska kosa
# Bela Stena
# Beli Potok (Voždovac)
# Beluće
# Besni Fok
# Bečmen
# Beljevac
# Beljina (Barajevo)
# Boždarevac
# Boleč
# Borča
# Boljevci
# Braće Jerković
# Brestovik
# Busije (Zemun)
# Velika Ivanča
# Velika Krsna
# Veliki Borak
# Veliko Selo (Palilula)
# Vidikovac (Rakovica)
# Vinča
# Vinča (Grocka)
# Višnjica
# Vlaška (Mladenovac)
# Vranić (Barajevo)
# Vrčin
# Glogonjski Rit
# Gornji Grad (Zemun)
# Granice (Mladenovac)
# Grmovac
# Guberevac (Sopot)
# Guncati (Barajevo)
# Dedinje
# Deponija (Beograd)
# Dobanovci
# Dorćol
# Donji Grad (Zemun)
# Dražanj
# Drlupa (Sopot)
# Dubona
# Dunavac
# Dučina
# Živkovac
# Zaklopača (Grocka)
# Zvezdara (Beograd)
# Zemun
# Zemun Polje
# Zuce
# Kalvarija (Zemun)
# Kaluđerica
# Kamendol
# Kanarevo brdo
# Karaburma
# Karton Siti
# Kijevo (Beograd)
# Kovačevac (Mladenovac)
# Kovilovo
# Kovilovo (Palilula)
# Kolonija Zmaj
# Koraćica
# Košutnjak
# Konjarnik (Beograd)
# Krnjača (Beograd)
# Kumodraž (selo)
# Kumodraž 2
# Labudovo brdo
# Ledine
# Leštane
# Lido (Zemun)
# Lisović
# Mala Vrbica (Mladenovac)
# Mala Ivanča
# Mali Požarevac
# Manić (Barajevo)
# Markovac (Mladenovac)
# Medaković
# Međulužje
# Meljak (Barajevo)
# Mirijevo
# Miljakovac
# Mladenovac (selo)
# Nemenikuće
# Nova Galenika
# Novi Grad (Zemun)
# Obrenovac
# Ovča
# Paviljoni
# Padinska Skela
# Parcani
# Pašino brdo
# Petrovčić
# Pinosava
# Plavi Horizonti
# Popović (Sopot)
# Progar
# Pružatovac
# Pudarci
# Rabrovac
# Rakovica (Beograd)
# Rajkovac (Mladenovac)
# Ralja (Sopot)
# Resnik
# Ripanj
# Ritopek
# Rogača (Sopot)
# Rožanci
# Ropočevo
# Senaja
# Senjak
# Sibnica (Sopot)
# Skojevsko naselje
# Slanci
# Slatina (Sopot)
# Sopot
# Stojnik (Sopot)
# Surčin
# Sutjeska (Zemun)
# Ugrinovci (Zemun)
# Umčari
# Cerak 2
# Cerak Vinogradi
# Crvenka (Beograd)
# Čubura (Beograd)
# Šepšin
# Šiljakovac
