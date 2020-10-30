from django.views.generic.base import TemplateView

from generic.mixins import CategoryListMixin


class DocumentsView(TemplateView, CategoryListMixin):
    template_name = 'documents/documents.html'
