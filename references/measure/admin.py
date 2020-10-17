from django.contrib import admin

from references.measure.models import Measure


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
