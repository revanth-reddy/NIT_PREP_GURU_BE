from django.contrib import admin
from .models import Slideshow, News, Companies, Exp
# Register your models here.

admin.site.register(Slideshow)
admin.site.register(News)
class CompAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Companies, CompAdmin)
class ExpAdmin(admin.ModelAdmin):
    list_display = ('name','placement', 'year', 'display')
admin.site.register(Exp, ExpAdmin)
