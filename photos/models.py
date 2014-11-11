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

    #is this a good solution (to set blan and null to true on ImageFields)
    #otherwise i can not make migrations
    medium_photo = models.ImageField(upload_to="photo_album/medium_size", blank= True, null=True)
    original_photo = models.ImageField(upload_to="photo_album/originals", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="photo_album/thumbnails", blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now=True)
    rating = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUS , default=ACCEPTED)
    city_part = models.CharField(choices=((x,x) for x in MUNICIPALITY),
                                 default = 'NEPOZNATO', max_length="51")

    # class Meta:
    #     ordering = ["pub_date"]

    def admin_thumbnail(self):
        # think about thumbnail size
        return u'<img src="{url}" />'.format(url=self.thumbnail.url)
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
        #if photo is "landscape"
        if w>h:
            min_side = w/max_side*h
            photo.thumbnail((max_side,min_side), Image.ANTIALIAS)
            return photo
        #if it's "portrait"
        else:
            min_side = h/max_side*w
            photo.thumbnail((min_side,max_side), Image.ANTIALIAS)
            return photo

    def _fill_img_field(self,img_field, max_side, img, photo_name):
        io = StringIO.StringIO()
        resized = self.resize(img,max_side)
        resized.save(io, format = resized.format)
        img_field.save(photo_name, ContentFile(io.getvalue()), save = False)
        pass

    def save(self):
        #From larger to smaller cuz we are working on the same
        #photo file. You cannot resize from smaller to larger.
        img = Image.open(self.original_photo.file)
        self._fill_img_field(self.medium_photo, 650, img, self.original_photo.name)
        self._fill_img_field(self.thumbnail, 200, img, self.original_photo.name)
        super(Post, self).save()

    def __unicode__(self):
        return self.description

# put names of city parts in a separate constants file
# DJURINCI,Djurinci
# JABUCKI_RIT,Jabučki Rit
# JAGNJILO,Jagnjilo (Mladenovac)
# JAKOVO,Jakovo
# JAJINCI,Jajinci
# ADA_MEDJICA,Ada Međica
# ALTINA<Altina
# AMERIC,Amerić
# ARNAJEVO,Arnajevo
# BABE,Babe (Sopot)
# BATAJNICA,Batajnica
# BANJICA,Banjica
# BACEVAC,Baćevac
# BEGALJICA,Begaljica
# BEZANIJA,Bežanija
# BEZANIJSKA_KOSA,Bežanijska kosa
# BELA_STENA,Bela Stena
# BELI_POTOK,Beli Potok (Voždovac)
# BELUCE,Beluće
# BESNI_FOK,Besni Fok
# BECMEN,Bečmen
# BELJEVACBeljevac
# BELJINA,Beljina (Barajevo)
# BOZDAREVAC,Boždarevac
# BOLEC,Boleč
# BORCA,Borča
# BOLJEVCI,Boljevci
# BRACE_JERKOVIC,Braće Jerković
# BRESTOVIK,Brestovik
# BUSIJE,Busije (Zemun)
# VELIKA_IVANCA,Velika Ivanča
# VELIKA_KRSNA,Velika Krsna
# VELIKI_BORAK,Veliki Borak
# VELIKO_SELO,Veliko Selo (Palilula)
# VIDIKOVAC,Vidikovac (Rakovica)
# VINCA,Vinča
# VINCA,Vinča (Grocka)
# VISNJICA,Višnjica
# VLASKA,Vlaška (Mladenovac)
# VRANIC,Vranić (Barajevo)
# VRCIN,Vrčin
# GLOGONJSKI_RIT,Glogonjski Rit
# GORNJI_GRAD,Gornji Grad (Zemun)
# GRANICE,Granice (Mladenovac)
# GRMOVAC,Grmovac
# GUBEREVAC,Guberevac (Sopot)
# GUNCATI,Guncati (Barajevo)
# DEDINJE,Dedinje
# DEPONIJA,Deponija (Beograd)
# DOBANOVCI,Dobanovci
# DORCOL,Dorćol
# DONJI_GRAD,Donji Grad (Zemun)
# DRAZANJ,Dražanj
# DRLUPA,Drlupa (Sopot)
# DUBONA,Dubona
# DUNAVAC,Dunavac
# DUCINA,Dučina
# ZIVKOVAC,Živkovac
# ZAKLOPACA,Zaklopača (Grocka)
# ZVEZDARA,Zvezdara (Beograd)
# ZEMUN,Zemun
# ZEMUN_POLJEZemun Polje
# ZUCE,Zuce
# KALVARIJA,Kalvarija (Zemun)
# KALUDJERICA,Kaluđerica
# KAMENDOL,Kamendol
# KANAREVO_BRDO,Kanarevo brdo
# KARABURMA, Karaburma
# KARTON_SITIKarton Siti
# KIJEVO,Kijevo (Beograd)
# KOVACEVAC,Kovačevac (Mladenovac)
# KOVILOVO,Kovilovo
# KOVILOVO_PALILULAKovilovo (Palilula)
# KOLONIJA_ZMAJ,Kolonija Zmaj
# KORACICA,Koraćica
# KOSUTNJAK,Košutnjak
# KONJARNIK,Konjarnik (Beograd)
# KRNJACA,Krnjača (Beograd)
# KUMODRAZ,Kumodraž (selo)
# KUMODRAZ_2,Kumodraž 2
# LABUDOVO_BRDO,Labudovo brdo
# LEDINE, Ledine
# LESTANJE, Leštane
# LIDO, Lido (Zemun)
# LISOVIC,Lisović
# MALA_VRBICA, Mala Vrbica (Mladenovac)
# MALA_IVANCA,Mala Ivanča
# MALI_POZAREVAC,Mali Požarevac
# MANIC,Manić (Barajevo)
# MARKOVAC, Markovac (Mladenovac)
# MEDAKOVIC, Medaković
# MEDJULUZJE,Međulužje
# MELJAK,Meljak (Barajevo)
# MIRIJEVO,Mirijevo
# MILJAKOVAC, Miljakovac
# MLADENOVAC,Mladenovac (selo)
# NEMENIKUCE,Nemenikuće
# NOVA_GALENIKA, Nova Galenika
# NOVI_GRAD,Novi Grad (Zemun)
# OBRENOVAC,Obrenovac
# OVCA,Ovča
# PAVILJONI,Paviljoni
# PADINSKA_SKELA,Padinska Skela
# PARCANI,Parcani
# PASINO_BRDO,Pašino brdo
# PETROVIC,Petrovčić
# PINOSAVA,Pinosava
# PLAVI_HORIZONT, Plavi Horizonti
# POPOVIC, Popović (Sopot)
# PROGAR, Progar
# PRUZATOVAC, Pružatovac
# PUDARCI, Pudarci
# RABROVAC, Rabrovac
# RAKOVICA,Rakovica (Beograd)
# RAJKOVAC,Rajkovac (Mladenovac)
# RALJA,Ralja (Sopot)
# RESNIK,Resnik
# RIPANJ,Ripanj
# RITOPEK,Ritopek
# ROGACA, Rogača (Sopot)
# ROZANCI,Rožanci
# ROPOCEVO,Ropočevo
# SENAJA,Senaja
# SENJAK, Senjak
# SIBNICA, Sibnica (Sopot)
# SKOJEVSKO_NASELJE, Skojevsko naselje
# SLANCI,Slanci
# SLATINA,Slatina (Sopot)
# SOPOT,Sopot
# STOJNIK,Stojnik (Sopot)
# SURCIN, Surčin
# SUTJESKA, Sutjeska (Zemun)
# UGRINOVCI, Ugrinovci (Zemun)
# UMCARI, Umčari
# CERAK_2,Cerak 2
# CERAK_VINOGRADI, Cerak Vinogradi
# (CRVENKA,"Crvenka (Beograd)"),
# (CUBURA, "Čubura (Beograd)"),
# (SEPSIN, "Šepšin"),
# (SILJAKOVAC,"Šiljakovac"))
