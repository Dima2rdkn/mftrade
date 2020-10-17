from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Measure


class MeasureListView(ListView):
    model = Measure
    template_name = 'references/measure/list.html'


class MeasureCreateView(CreateView):
    model = Measure
    fields = '__all__'
    template_name = 'references/measure/detail.html'
    success_url = reverse_lazy('references:measure_list')


class MeasureUpdateView(UpdateView):
    model = Measure
    fields = '__all__'
    template_name = 'references/measure/detail.html'
    success_url = reverse_lazy('references:measure_list')


class MeasureDeleteView(DeleteView):
    model = Measure
    template_name = 'references/measure/confirm.html'
    success_url = reverse_lazy('references:measure_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_object()
            try:
                queryset.delete()
            except ProtectedError:
                error = 1
                return render(request, 'references/measure/confirm.html',
                              {'error': error})
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)
