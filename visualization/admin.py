from django.contrib.gis import admin
from . import models


class GadmAdmin(admin.GeoModelAdmin):
    search_fields = ['name_engli']
    list_display = ['id_0', 'name_engli',]

admin.site.register(models.GADM, GadmAdmin)
