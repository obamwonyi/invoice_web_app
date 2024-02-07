from rest_framework import serializers
from .models import Client

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