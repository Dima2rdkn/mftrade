from django.contrib import admin

from references.stock.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
