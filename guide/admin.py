from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class GuideImageInline(admin.TabularInline):
    model = GuideImage
    extra = 0

    class StatusAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_active', 'created']
        list_editable = ['is_active']
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = GuideStatus

    admin.site.register(GuideStatus, StatusAdmin)


class GuideResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(GuideStatus,
                                                                                            'name'))

    class Meta:
        model = Guide
        exclude = ['id', 'is_active', 'updated', 'created']


class GuideAdmin(ImportExportActionModelAdmin):
    save_as = True
    resource_class = GuideResource
    fields = [('first_name', 'last_name', 'status'), ('country', 'town'), ('phone', 'email'), 'dob', 'description',
              ('vk', 'instagram', 'twitter', 'facebook'), 'is_active']
    list_display = ['first_name', 'last_name', 'status', 'is_active']
    list_editable = ['status', 'is_active']
    inlines = [GuideImageInline]
    list_filter = ['status', 'is_active']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Guide


admin.site.register(Guide, GuideAdmin)


class GuideImageAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['guide', 'image', 'is_main', 'is_active', 'created']
    list_editable = ['is_main', 'is_active']
    list_filter = ['is_main', 'is_active', 'guide']
    # change_list_template = ['guide']

    class Meta:
        model = GuideImage


admin.site.register(GuideImage, GuideImageAdmin)
