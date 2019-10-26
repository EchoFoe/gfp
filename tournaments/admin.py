from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class TournamentImageInline(admin.TabularInline):
    model = TournamentImage
    extra = 0

    class StatusAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_active', 'created']
        list_editable = ['is_active']
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = TournamentStatus

    admin.site.register(TournamentStatus, StatusAdmin)


class TournamentResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(TournamentStatus,
                                                                                            'name'))

    class Meta:
        model = Tournament
        exclude = ['id', 'is_active', 'description', 'updated', 'created', 'provisions_dk', 'provisions_bezdk',
                   'nominations', 'name']


class TournamentAdmin (ImportExportActionModelAdmin):
    save_as = True
    resource_class = TournamentResource
    fields = [('name', 'short_name', 'status'), ('country', 'region', 'town'), ('start_time', 'end_time'),
              'sponsors', 'description', ('provisions_dk', 'provisions_bezdk', 'nominations'), ('photo_vk', 'video_youtube'), 'is_active']
    list_display = ['Турнир', 'town', 'start_time', 'end_time', 'status']
    list_editable = ['status', 'start_time', 'end_time']
    inlines = [TournamentImageInline]
    list_filter = ['status', 'is_active', 'town']
    search_fields = ['name']

    class Meta:
        model = Tournament


admin.site.register(Tournament, TournamentAdmin)


class TournamentImageAdmin (admin.ModelAdmin):
    save_as = True
    list_display = ['tournament', 'image', 'is_main', 'is_active', 'created']
    list_editable = ['is_main', 'is_active']
    list_filter = ['is_main', 'is_active', 'tournament']
    change_list_template = ['tournament']

    class Meta:
        model = TournamentImage


admin.site.register(TournamentImage, TournamentImageAdmin)