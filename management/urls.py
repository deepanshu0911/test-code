from django.urls import path
from management import views

urlpatterns = [
    path('create-expense', views.createExpense, name="create-expense"),
    path('print-expenses', views.printExpenses, name="print-expenses"),
    path('print-expense-by-id', views.printExpenseById, name="print-expense-by-id"),
    path('print-expenses-by-search', views.printExpensesBySearch, name="print-expenses-by-search"),
    path('update-expense', views.updateExpense, name="update-expense"),
    path('delete-expenses', views.deleteExpenses, name="delete-expenses"),

    path('create-supplier', views.createSupplier, name="create-supplier"),
    path('print-suppliers', views.printSuppliers, name="print-supplier"),
    path('print-supplier-by-id', views.printSupplierById, name="print-supplier-by-id"),
    path('print-suppliers-by-search', views.printSuppliersBySearch, name="print-supplier-by-search"),
    path('update-supplier', views.updateSupplier, name="update-supplier"),
    path('delete-suppliers', views.deleteSuppliers, name="delete-supplier"),

    path('create-purchase', views.createPurchase, name="create-purchase"),
    path('update-purchase', views.updatePurchase, name="update-purchase"),
    path('print-purchases', views.printPurchases, name="print-purchases"),
    path('print-purchases-by-search', views.printPurchasesBySearch, name="search-purchases"),
    path('print-purchase-by-id', views.printPurchaseById, name="print-purchase-by-id"),
    path('delete-purchases', views.deletePurchases, name='delete-purchases'),

    path('return-purchase-data', views.getReturnPurchase, name="return-purchase-data"),
    path('return-purchase', views.returnPurchase, name='return-purchase'),
  

    path('save-purchase-file', views.savePurchaseFile, name="save-purchase-file"),
    path('print-file-by-id', views.printFileById, name="print-file-by-id"),
    path('update-file', views.updateFile, name="update-file"),
]