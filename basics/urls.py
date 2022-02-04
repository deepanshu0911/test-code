from django.urls import path
from basics import views

urlpatterns = [
  path('create-company', views.companyCreate, name="create-company"),
  path('print-company', views.printCompany, name="print-company"),
  
  path('create-tax', views.taxCreate, name="create-tax"),
  path('print-taxes', views.printTaxes, name="print-taxes"),
  path('delete-taxes', views.deleteTaxes, name="delete-taxes"),
  
  path('create-unit', views.unitCreate, name='create-unit'),
  path('print-units', views.printUnits, name='print-units'),
  path('delete-units', views.deleteUnits, name='delete-units'),

  path('best-sellers', views.bestSeller, name="best-sellers"),
  path('stock-alerts', views.stockAlerts, name="stock-alerts"),
  path('last-month-sales', views.lastMonthSales, name="last-month-sales"),
  path('sales-report', views.salesReport, name="sales-report"),
  path('items-report', views.itemsReport, name="items-report"),

  path('create-help', views.createHelp, name="create-help"),
  path('print-helps', views.printHelp, name="print-help"),
]