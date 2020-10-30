from django.db import transaction
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Invoice
from .forms import InvoiceEditForm, InvoiceEditFormSet


class InvoiceListView(ListView):
    model = Invoice
    queryset = Invoice.objects.filter(status='inventory')
    template_name = 'documents/invoice/list.html'


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceEditForm
#    fields = ['number', 'invoice_date', 'supplier', 'stock']
    template_name = 'documents/invoice/detail.html'
    success_url = reverse_lazy('documents:inventory')

    def get_context_data(self, **kwargs):
        data = super(InvoiceCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['invoicetable'] = InvoiceEditFormSet(self.request.POST)
        else:
            data['invoicetable'] = InvoiceEditFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoicetable = context['invoicetable']
        with transaction.atomic():
            form.instance.user = self.request.user
            form.instance.status = Invoice.STATUS_CHOICES.inventory
            self.object = form.save()
            if invoicetable.is_valid():
                invoicetable.instance = self.object
                invoicetable.save()
        return super(InvoiceCreateView, self).form_valid(form)


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'documents/invoice/confirm.html'
    success_url = reverse_lazy('documents:inventory')
