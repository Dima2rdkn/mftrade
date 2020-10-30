from django.urls import path

from documents.views import DocumentsView
from documents.invoice import views as invoice_views

app_name = 'documents'

urlpatterns = [
    path('', DocumentsView.as_view(), name='main'),
    path('inventory/', invoice_views.InvoiceListView.as_view(),
         name='inventory'),
    path('inventory/new/', invoice_views.InvoiceCreateView.as_view(),
         name='inventory_new'),
    path('inventory/<int:pk>/delete',invoice_views.InvoiceDeleteView.as_view(),
         name='inventory_delete')
]
