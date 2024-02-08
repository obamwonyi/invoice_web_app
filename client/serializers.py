from rest_framework import serializers
from .models import Client
from invoice.models import Invoice



class ClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            "id",
            "invoice_number",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "get_due_date_formatted",
            "invoice_type",
            "is_credited",
        )


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client

        # fields that would not be modifiable
        # note the id field is added automatically by Django/python
        read_on_fields = (
            "created_at",
            "created_by",
        ),

        # fields that we can access / and see
        fields = (
            "id",
            "name",
            "email",
            "org_number",
            "address1",
            "address2",
            "zipcode",
            "place",
            "country",
            "contact_person",
            "contact_reference"
        )