from django.contrib import admin

# Register your models here.

from .models import Invoice, Item

# Register your models here.
admin.site.register(Invoice)

admin.site.register(Item)