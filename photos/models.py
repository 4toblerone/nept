#coding: utf-8
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
    photo = models.ImageField(upload_to="photo_album")
    pub_date = models.DateTimeField('date published', auto_now=True)
    rating = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUS , default=ACCEPTED)
    city_part = models.CharField(choices=((x,x) for x in MUNICIPALITY),
                                 default = 'NEPOZNATO', max_length="51")

    def admin_thumbnail(self):
        # think about thumbnail size
        return u'<img src="{url}" width="100" height="100" />'.format(url=self.photo.url)
    admin_thumbnail.short_description = "Thumbnail"
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.description

    #override Model save method with custom one
    #which will create thumbnail before saving post

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
