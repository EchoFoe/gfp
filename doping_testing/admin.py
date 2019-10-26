from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class DopingAdmin(admin.ModelAdmin):
    list_display = ['laboratory', 'is_active']
    list_editable = ['is_active']
    list_filter = ['laboratory']

    class Meta:
        model = Doping


admin.site.register(Doping, DopingAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created']
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = AutopsyStatus


admin.site.register(AutopsyStatus, StatusAdmin)


class AutopsyResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(AutopsyStatus,
                                                                                            'name'))

    class Meta:
        model = Autopsy
        exclude = ['id', 'is_active', 'updated', 'created']


class AutopsyAdmin (ImportExportActionModelAdmin):
    save_as = True
    resource_class = AutopsyResource
    fields = [('first_name', 'last_name', 'middle_name'), 'status', ('phone', 'email'), 'dob', ('created', 'updated')]
    list_display = ['last_name', 'first_name', 'dob', 'phone', 'email', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ['first_name', 'last_name', 'middle_name']


    class Meta:
        model = Autopsy


admin.site.register(Autopsy, AutopsyAdmin)