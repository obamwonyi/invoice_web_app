
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models

class Invoice(models.Model):
    # declaring invoice constant, noticed there are no key words for constant in python
    INVOICE = 'invoice'
    # constant
    CREDIT_NOTE = 'credit_note'

    # simply mapping the values to user readable forms
    CHOICES_TYPE = (
        (INVOICE, 'Invoice'),
        (CREDIT_NOTE, 'Credit note')
    )

    invoice_number = models.IntegerField(default=1)
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    client_org_number = models.CharField(max_length=255, blank=True, null=True)
    client_address1 = models.CharField(max_length=255, blank=True, null=True)
    client_address2 = models.CharField(max_length=255, blank=True, null=True)
    client_zipcode = models.CharField(max_length=255, blank=True, null=True)
    client_place = models.CharField(max_length=255, blank=True, null=True)
    client_country = models.CharField(max_length=255, blank=True, null=True)
    client_contact_person = models.CharField(max_length=255, blank=True, null=True)
    client_contact_reference = models.CharField(max_length=255, blank=True, null=True)
    sender_reference = models.CharField(max_length=255, blank=True, null=True)
    invoice_type = models.CharField(max_length=20, choices=CHOICES_TYPE, default=INVOICE)
    due_days = models.IntegerField(default=14)
    is_credit_for = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_credited = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    bankaccount = models.CharField(max_length=266, blank=True, null=True)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    team = models.ForeignKey("teams.Team", related_name='invoices', on_delete=models.CASCADE)
    client = models.ForeignKey("client.Client", related_name='invoices', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='created_invoices', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        """
        Configures query_set of the invoice to be ordered by the created_at
        in descending order.
        """
        ordering = ('-created_at',)
    
    
    def get_due_date(self):
        return self.created_at + timedelta(days=self.due_days)
    
    def get_due_date_formatted(self):
        return self.get_due_date().strftime("%d.%m.%Y")
