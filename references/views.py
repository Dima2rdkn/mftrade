from django.views.generic.base import TemplateView

from generic.mixins import CategoryListMixin


# Create your views here.


class ReferencesView(TemplateView, CategoryListMixin):
    template_name = 'references/references.html'
