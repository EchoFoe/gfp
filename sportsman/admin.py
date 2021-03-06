from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created']
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discipline._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Discipline


admin.site.register(Discipline, DisciplineAdmin)


class Weight_categoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Weight_category._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Weight_category


admin.site.register(Weight_category, Weight_categoryAdmin)


class Age_categoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Age_category._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Age_category


admin.site.register(Age_category, Age_categoryAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Division._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Division


admin.site.register(Division, DivisionAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gender._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Gender


admin.site.register(Gender, GenderAdmin)


class Line_upAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Line_up._meta.fields]
    list_editable = ['is_active']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Line_up


admin.site.register(Line_up, Line_upAdmin)


class SportsmenResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(Status,
                                                                                            'name'))
    gender = fields.Field(column_name='gender', attribute='gender', widget=ForeignKeyWidget(Gender, 'name'))
    discipline = fields.Field(column_name='discipline', attribute='discipline',
                              widget=ForeignKeyWidget(Discipline, 'name'))
    division = fields.Field(column_name='division', attribute='division', widget=ForeignKeyWidget(Division, 'name'))
    line_up = fields.Field(column_name='line_up', attribute='line_up', widget=ForeignKeyWidget(Line_up, 'name'))
    weight = fields.Field(column_name='weight', attribute='weight', widget=ForeignKeyWidget(Weight_category, 'name'))
    age = fields.Field(column_name='age', attribute='age', widget=ForeignKeyWidget(Age_category, 'name'))
    tournament = fields.Field(column_name='tournament', attribute='tournament', widget=ForeignKeyWidget(Tournament, 'name'), )

    class Meta:
        model = Sportsman
        exclude = ['id', 'is_active', 'updated', 'created']


class SportsmenAdmin(ImportExportActionModelAdmin):
    save_as = True
    resource_class = SportsmenResource
    fields = [('last_name', 'first_name', 'middle_name'), ('phone', 'email', 'gender'), ('country', 'region', 'town'), ('dob', 'age'), ('weight', 'raised_weight', 'wilkes'), 'division', 'discipline', 'tournament', ('team', 'team_name'), 'status', 'is_active', ('created', 'updated')]
    list_display = ['last_name', 'first_name', 'age', 'weight', 'is_active', 'wilkes', 'team_name']
    list_editable = ['is_active', 'wilkes', 'team_name']
    list_filter = ['tournament', 'division', 'discipline', 'gender', 'status']
    search_fields = ['first_name', 'last_name', 'middle_name']

    class Meta:
        model = Sportsman


admin.site.register(Sportsman, SportsmenAdmin)


# class TournamentImageInline(admin.TabularInline):
#     model = TournamentImage
#     extra = 0
#
#     class StatusAdmin(admin.ModelAdmin):
#         list_display = ['name', 'is_active', 'created']
#         list_editable = ['is_active']
#         list_filter = ['name']
#         search_fields = ['name']
#
#         class Meta:
#             model = TournamentStatus
#
#     admin.site.register(TournamentStatus, StatusAdmin)
#
#
# class TournamentResource(resources.ModelResource):
#     status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(TournamentStatus,
#                                                                                             'name'))
#
#     class Meta:
#         model = Tournament
#         exclude = ['id', 'is_active', 'description', 'updated', 'created', 'provisions_dk', 'provisions_bezdk',
#                    'nominations', 'name']
#
#
# class TournamentAdmin (ImportExportActionModelAdmin):
#     save_as = True
#     resource_class = TournamentResource
#     fields = [('name', 'short_name', 'status'), ('country', 'region', 'town'), ('start_time', 'end_time'),
#               'sponsors', 'description', ('provisions_dk', 'provisions_bezdk', 'nominations'), ('photo_vk', 'video_youtube'), 'is_active']
#     list_display = ['Турнир', 'town', 'start_time', 'end_time', 'status']
#     list_editable = ['status', 'start_time', 'end_time']
#     inlines = [TournamentImageInline]
#     list_filter = ['status', 'is_active', 'town']
#     search_fields = ['name']
#
#     class Meta:
#         model = Tournament
#
#
# admin.site.register(Tournament, TournamentAdmin)
#
#
# class TournamentImageAdmin (admin.ModelAdmin):
#     save_as = True
#     list_display = ['tournament', 'image', 'is_main', 'is_active', 'created']
#     list_editable = ['is_main', 'is_active']
#     list_filter = ['is_main', 'is_active', 'tournament']
#     change_list_template = ['tournament']
#
#     class Meta:
#         model = TournamentImage
#
#
# admin.site.register(TournamentImage, TournamentImageAdmin)
