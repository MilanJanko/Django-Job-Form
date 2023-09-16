from django.contrib import admin
from . import models


class AdminForm(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')
    search_fields = ('first_name', 'last_name', 'email', 'date', 'occupation')
    list_filter = ('date', 'occupation')
    ordering = ('first_name',)


admin.site.register(models.Form, AdminForm)
