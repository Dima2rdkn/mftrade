from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Stock


class StockListView(ListView):
    model = Stock
    template_name = 'references/stock/list.html'


class StockCreateView(CreateView):
    model = Stock
    fields = '__all__'
    template_name = 'references/stock/detail.html'
    success_url = reverse_lazy('references:stock_list')


class StockUpdateView(UpdateView):
    model = Stock
    fields = '__all__'
    template_name = 'references/stock/detail.html'
    success_url = reverse_lazy('references:stock_list')


class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'references/stock/confirm.html'
    success_url = reverse_lazy('references:stock_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_object()
            try:
                queryset.delete()
            except ProtectedError:
                error = 1
                return render(request, 'references/stock/confirm.html',
                              {'error': error})
        return HttpResponseRedirect(self.success_url)
