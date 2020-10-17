from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Contragent


class ContragentListView(ListView):
    model = Contragent
    template_name = 'references/contragent/list.html'


class ContragentCreateView(CreateView):
    model = Contragent
    fields = '__all__'
    #    form_class = ContragentCreateForm
    template_name = 'references/contragent/detail.html'
    success_url = reverse_lazy('references:contragent_list')


class ContragentUpdateView(UpdateView):
    model = Contragent
    fields = '__all__'
    template_name = 'references/contragent/detail.html'
    success_url = reverse_lazy('references:contragent_list')


class ContragentDeleteView(DeleteView):
    model = Contragent
    template_name = 'references/contragent/confirm.html'
    success_url = reverse_lazy('references:contragent_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_object()
            try:
                queryset.delete()
            except ProtectedError:
                error = 1
                return render(request, 'references/contragent/confirm.html',
                              {'error': error})
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)
