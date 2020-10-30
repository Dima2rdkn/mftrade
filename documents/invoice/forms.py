from django.forms import ModelForm, inlineformset_factory
from .models import Invoice, InvoiceTable


class InvoiceEditForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = ('user', 'status', 'summa')


InvoiceEditFormSet = inlineformset_factory(Invoice, InvoiceTable,
                                           form=InvoiceEditForm,
                                           can_delete=True,
                                           can_order=True,
                                           extra=1,
                                           )
items_formset = InvoiceEditFormSet
item_forms = items_formset()
