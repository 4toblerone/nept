from django.conf.urls import patterns, url
import views

urlpatterns= patterns('',
                     url(r'^dosta/',views.d, name = 'd'),
                     url(r"^$", views.index, name="index"),
                     url(r'^return_next_posts', views.return_next_posts,  name ='return_next_posts')
                     )