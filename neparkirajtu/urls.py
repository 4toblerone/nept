from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neparkirajtu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.BASE_DIR + settings.MEDIA_URL}),
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('photos.urls',namespace='photos')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
