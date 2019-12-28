from django.contrib import admin
from .models import Slideshow, News, Companies
# Register your models here.

admin.site.register(Slideshow)
admin.site.register(News)
class CompAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Companies, CompAdmin)
