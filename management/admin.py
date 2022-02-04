from django.contrib import admin
from management.models import Expense, Supplier, Purchase, purchaseFile

admin.site.register(Expense)
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(purchaseFile)