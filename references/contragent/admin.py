from django.contrib import admin

from references.contragent.models import Contragent


@admin.register(Contragent)
class ContragentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
