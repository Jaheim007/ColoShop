from django.contrib import admin
from .models import NewsLetter, Banner, Site_Info, Info

@admin.register(NewsLetter)
class News(admin.ModelAdmin):

    list_display = ('email',)

@admin.register(Site_Info)
class Site(admin.ModelAdmin):

    list_display = (
        'Site_name',
        'Section_New_Arrivals_Title',
        'Section_Deals_Title',
        'Copyright'
    )

@admin.register(Banner)
class Banner(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'Image'
    )

@admin.register(Info)
class Info(admin.ModelAdmin):

    list_display = (
        'title',
        'icon',
        'description'
    )