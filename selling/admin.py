from django.contrib import admin
from selling.models import Item, Client, Invoice, Quotation, billFile, quoteFile

admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Quotation)
admin.site.register(billFile)
admin.site.register(quoteFile)
