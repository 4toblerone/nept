from django.contrib import admin
from models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    fields = ['description','city_part', 'rating','status','photo']
    list_display = ('admin_thumbnail', 'description', 'rating', 'status', 'city_part')

admin.site.register(Post,PostAdmin)