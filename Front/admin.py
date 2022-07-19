from django.contrib import admin
from .models import NewsLetter, Banner, Site_Info, Service, Contact

@admin.register(NewsLetter)
class News(admin.ModelAdmin):

    list_display = (
        'email',
    )
    
@admin.register(Contact)
class Contact(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'website',
        'message'
    )

@admin.register(Site_Info)
class Site(admin.ModelAdmin):

    list_display = (
        'site_name',
        'section_new_arrivals_title',
        'section_deals_title',
        'opening_days',
        'email',
        'closed_day',
        'phone',
        'copyright',
        'map_location',
    )

@admin.register(Banner)
class Banner(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'product_on_promotion'
    )

@admin.register(Service)
class Service(admin.ModelAdmin):

    list_display = (
        'title',
        'icon',
        'description'
    )