from django.conf.urls import patterns, url
import views

urlpatterns= patterns('',
                     url(r'^dosta/',views.d, name = 'd'),
                     url(r"^$", views.index, name="index"),
                     )