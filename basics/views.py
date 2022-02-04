from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q
from basics.models import CompanyProfile, Tax, Unit, Help
from basics.serializers import CompanyProfileSerializer, TaxSerializer, UnitSerializer, HelpSerializer
from selling.models import Item, Invoice
from selling.serializers import ItemSerializer, InvoiceSerializer
from datetime import date, timedelta

# Company Profile handling starts
@csrf_exempt
def companyCreate(request):
  if request.method == "POST":
    data = JSONParser().parse(request)
    if not CompanyProfile.objects.filter(created="already").exists():
       company = CompanyProfile(company_name=data['companyName'],
         mobile=data['mobile'], address=data['address'], city=data['city'],
         state=data['state'], pincode=data['pincode'], email=data['email'],
         mobile2=data['mobile2'], website=data['website'])
       if data['gstin']:
        company.gstin = data['gstin'].upper()
       company.save() 
       return JsonResponse({'status': 'created'}, safe=False)
    else:
      try:
        company = CompanyProfile.objects.get(company_id=data['companyId'])
        if data['gstin']:
            company.gstin = data['gstin'].upper()
            print(company.gstin)
        company.save()    
        CompanyProfile.objects.filter(company_id=data['companyId']).update(company_name=data['companyName'],
         mobile=data['mobile'], address=data['address'], city=data['city'],
         state=data['state'], pincode=data['pincode'], email=data['email'],
         mobile2=data['mobile2'], website=data['website'])
        return JsonResponse({'status': 'updated'}, safe=False)
      except:
        return JsonResponse({'status': 'error'}, safe=False)   

def printCompany(request):
    if request.method == "GET":
        company = CompanyProfile.objects.all()
        companyData = CompanyProfileSerializer(company, many=True)
        return JsonResponse(companyData.data, safe=False)

# Company Profile handling ends

# Tax handling starts
@csrf_exempt
def taxCreate(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if not Tax.objects.filter(tax_name=data['taxName'].upper(), tax_rate=data['taxRate']).exists():
            Tax.objects.create(tax_name=data['taxName'].upper(), tax_rate=data['taxRate'])  
            return JsonResponse({'status': 'created'}, safe=False)
        else:
            return JsonResponse({'status': 'exists'}, safe=False)


def printTaxes(request):
    if request.method == "GET":
       taxes = Tax.objects.all()
       taxesData = TaxSerializer(taxes, many=True)
       return JsonResponse(taxesData.data, safe=False)     
 
@csrf_exempt
def deleteTaxes(request):
 if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Tax.objects.filter(tax_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Tax handling ends

# Unit handling starts
@csrf_exempt
def unitCreate(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if not Unit.objects.filter(unit_name=data['unitName'], unit_qty=data['unitQty']).exists():
            Unit.objects.create(unit_name=data['unitName'], unit_qty=data['unitQty'])  
            return JsonResponse({'status': 'created'}, safe=False)
        else:
            return JsonResponse({'status': 'exists'}, safe=False)


def printUnits(request):
    if request.method == "GET":
       units = Unit.objects.all()
       unitsData = UnitSerializer(units, many=True)
       return JsonResponse(unitsData.data, safe=False)   

@csrf_exempt
def deleteUnits(request):
 if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Unit.objects.filter(unit_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)           

# Unit handling ends

# Charts handling starts
def bestSeller(request):
    if request.method == "GET":
        items = Item.objects.all().order_by('-qty_sold')[:10]
        itemData = ItemSerializer(items, many=True)
        return JsonResponse({'status': 'success', 'result': itemData.data}, safe=False)

def stockAlerts(request):
    if request.method == "GET":
        items = Item.objects.filter(stock_qty__lte=10)[:12]
        itemData = ItemSerializer(items, many=True)
        return JsonResponse({'status': 'success', 'result': itemData.data}, safe=False)

def lastMonthSales(request):
    if request.method == "GET":
        endDate = date.today()
        startDate = endDate - timedelta(days=7)
        invoices = Invoice.objects.filter(created_date__range=[startDate, endDate])
        invoicesData = InvoiceSerializer(invoices, many=True)
        return JsonResponse({'status': 'success', 'result': invoicesData.data}, safe=False)


# Charts handling ends


# Downloadable reports starts
@csrf_exempt
def salesReport(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        month = data['month']
        status = data['status']
        if status != 'All':
         invoices = Invoice.objects.filter(created_date__month=int(month), status=status)
        if status == 'All': 
         invoices = Invoice.objects.filter(created_date__month=int(month))
        invoicesData = InvoiceSerializer(invoices, many=True)
        return JsonResponse({'status': 'success', 'result': invoicesData.data}, safe=False)

@csrf_exempt
def itemsReport(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        month = data['month']
        status = data['status']
        if month != 'All':
          if status=='All':
              items = Item.objects.filter(created_date__month=int(month))
          if status=='In stock':
              items = Item.objects.filter(created_date__month=int(month), stock_qty__gte=10)
          if status=='Out of stock':
              items = Item.objects.filter(created_date__month=int(month), stock_qty__lte=10)
        elif month=='All':
          if status=='All':
              items = Item.objects.all()
          if status=='In stock':
              items = Item.objects.filter(stock_qty__gte=10)
          if status=='Out of stock':
              items = Item.objects.filter(stock_qty__lte=10)        
        itemsData = ItemSerializer(items, many=True)
        return JsonResponse({'status': 'success', 'result': itemsData.data}, safe=False)

# Downloadable reports ends

# Help starts
@csrf_exempt
def createHelp(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        Help.objects.create(category=data['category'], description=data['description'])
        return JsonResponse({"status": 'success'}, safe=False)

def printHelp(request):
    if request.method == "GET":
     helps = Help.objects.all().order_by('-help_id')[:10]
     helpsData = HelpSerializer(helps, many=True)
     return JsonResponse({'status': 'success', 'result': helpsData.data}, safe=False)

# Help ends