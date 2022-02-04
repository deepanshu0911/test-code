from django.urls import path
from selling import views

urlpatterns = [
    path('create-client', views.createClient, name="create-client"),
    path('print-clients', views.printClients, name="print-clients"),
    path('print-client-by-id', views.printClientById, name="client-by-id"),
    path('print-clients-by-search', views.printClientsBySearch, name="print-clients-by-search"),
    path('update-client', views.updateClient, name="update-client"),
    path('delete-clients', views.deleteClients, name='delete-clients'),

    path('create-item', views.createItem, name="create-item"),
    path('print-items', views.printItems, name="print-items"),
    path('print-item-by-id', views.printItemById, name="print-item-by-id"),
    path('print-items-by-search', views.printItemsBySearch, name="print-items-by-search"),
    path('search-item', views.searchItem, name="search-item"),
    path('searching-item/<str:search>', views.searchingItem, name="searching-item"),
    path('update-item', views.updateItem, name="update-item"),
    path('delete-items', views.deleteItems, name='delete-items'),

    path('create-invoice', views.createInvoice, name="create-invoice"),
    path('update-invoice', views.updateInvoice, name="update-invoice"),
    path('print-invoices', views.printInvoices, name="print-invoices"),
    path('print-invoices-by-search', views.printInvoicesBySearch, name="search-invoice"),
    path('print-invoice-by-id', views.printInvoiceById, name="print-invoice-by-id"),
    path('delete-invoices', views.deleteInvoices, name='delete-invoices'),

    path('return-invoice-data', views.getReturnInvoice, name="return-invoice-data"),
    path('return-invoice', views.returnInvoice, name='return-invoice'),
    
    path('save-bill-file', views.saveBillFile, name="save-bill-file"),
    path('print-bill-by-id', views.printBillById, name="print-bill-by-id"),
    path('update-bill-file', views.updateBillFile, name="update-bill-file"),
  
    path('create-quotation', views.createQuotation, name="create-quotation"),
    path('print-quotations', views.printQuotations, name="print-quotes"),
    path('print-quotations-by-search', views.printQuotationsBySearch, name="print-quotations-by-search"),
    path('delete-quotations', views.deleteQuotations, name="delete-quotation"),

    path('save-quote-file', views.saveQuoteFile, name="save-quote-file"),
    path('print-quote-file-by-id', views.printQuoteFileById, name="print-quote-file-by-id"),
    path('update-quote-file', views.updateQuoteFile, name="update-quote-file"),
 
]