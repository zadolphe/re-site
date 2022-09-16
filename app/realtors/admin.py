from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Realtor, RealtorAdmin)