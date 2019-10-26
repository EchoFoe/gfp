from django.contrib import admin
from .models import *


class DocumentAdmin (admin.ModelAdmin):
    save_as = True
    fields = ['name', 'rules', 'rules_sfo', 'standards', 'sports_regulations', 'norms_sports_titles_dk', 'norms_sports_titles_bez_dk', 'tests_secretary', 'tests_judge', 'is_active', ('created', 'updated')]
    list_display = ['name', 'is_active', 'created']
    list_editable = ['is_active']
    list_filter = ['name', 'is_active']
    search_fields = ['name']

    class Meta:
        model = Document


admin.site.register(Document, DocumentAdmin)