from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'realtor', 'is_published', 'list_date')
    list_display_links = ('id', 'title', 'realtor')
    list_filter = ('realtor',)
    search_fields = ('title', 'city', 'address', 'state')

admin.site.register(Listing, ListingAdmin)
