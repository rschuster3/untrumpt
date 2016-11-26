from django.contrib import admin
from .models import *

class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Organization, OrganizationAdmin)
