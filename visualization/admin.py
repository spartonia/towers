from django.contrib.gis import admin
from . import models


class GadmAdmin(admin.GeoModelAdmin):
    search_fields = ['name_engli']
    list_display = ['name_engli']

admin.site.register(models.GADM, GadmAdmin)


class Gadm1Admin(admin.GeoModelAdmin):
    search_fields = ['name_1']
    list_display = ['name_1', 'enabled']
    list_editable = ['enabled']

admin.site.register(models.GADM1, Gadm1Admin)


class Gadm2Admin(admin.GeoModelAdmin):
    search_fields = ['name_2']
    list_display = ['name_2', 'enabled']
    list_editable = ['enabled']
    list_filter = ['name_1', 'enabled']

admin.site.register(models.GADM2, Gadm2Admin)