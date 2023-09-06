from django.contrib import admin
from .models import Information
from import_export import resources 
from import_export.admin import ImportExportModelAdmin 


class InformationResource(resources.ModelResource):

    class Meta:
        model = Information

class InformationAdmin(ImportExportModelAdmin):
    resource_class = InformationResource


admin.site.register(Information,InformationAdmin)