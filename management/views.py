from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q
from django.core.paginator import Paginator
from decimal import Decimal
import json
from management.models import Expense, Supplier, Purchase, purchaseFile
from management.serializers import ExpenseSerializer, SupplierSerializer, PurchaseSerializer, PurchaseFileSerializer
from selling.models import Item

# Expense handling starts
@csrf_exempt
def createExpense(request):
    if request.method=="POST":
         data = JSONParser().parse(request)
         Expense.objects.create(expense_no=data['expenseNo'], category=data['category'],
                            expense_for=data['expenseFor'], amount=data['amount'], 
                            note=data['note'], expense_date=data['expenseDate'])
         return JsonResponse({'status': 'created'}, safe=False)                   

@csrf_exempt
def printExpenses(request):
  if request.method=="POST":
      data = JSONParser().parse(request)
      expenses = Expense.objects.all().order_by('-expense_id')
      p = Paginator(expenses,10)
      try:
          expenses = p.page(data['page'])
          expensesData = ExpenseSerializer(expenses, many=True)
          return JsonResponse({'status': 'success', 'result': expensesData.data, 'page':data['page']}, safe=False)
      except:
           return JsonResponse({'status': 'not-found'})

@csrf_exempt
def printExpenseById(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        expense = Expense.objects.filter(expense_id=data['expense_id'])
        expenseData = ExpenseSerializer(expense, many=True)
        return JsonResponse({'status': 'success', 'result': expenseData.data}, safe=False)

@csrf_exempt
def printExpensesBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        expenses = Expense.objects.filter(Q(expense_no__icontains=term)|
                   Q(expense_for__icontains=term)|Q(expense_id__iexact=term)|
                   Q(category__icontains=term)|Q(amount__icontains=term)
                   |Q(note__icontains=term)).order_by('-expense_id')
        expensesData = ExpenseSerializer(expenses, many=True)
        return JsonResponse({'status': 'success', 'result': expensesData.data}, safe=False)           


@csrf_exempt
def updateExpense(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        Expense.objects.filter(expense_id=data['expense_id']).update(expense_no=data['expenseNo'], category=data['category'],
                            expense_for=data['expenseFor'], amount=data['amount'], 
                            note=data['note'], expense_date=data['expenseDate'])
        return JsonResponse({'status': 'updated'}, safe=False)

@csrf_exempt
def deleteExpenses(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Expense.objects.filter(expense_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Expense handling ends

# Supplier handling starts
@csrf_exempt
def createSupplier(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if not Supplier.objects.filter(supplier_name=data['supplierName']).exists():
            Supplier.objects.create(supplier_name=data['supplierName'], mobile=data['mobile'],
                            whatsappNo=data['whatsapp'], email=data['email'], address=data['address'],
                            city=data['city'], state=data['state'], pincode=data['pincode'], gstin=data['gstin'])
            return JsonResponse({'status': 'created'}, safe=False)
        else: 
            return JsonResponse({'status': 'exists'}, safe=False)   

@csrf_exempt
def printSuppliers(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        suppliers = Supplier.objects.all().order_by('-supplier_id')
        p = Paginator(suppliers,10)
        try:
          suppliers = p.page(data['page'])
          suppliersData = SupplierSerializer(suppliers, many=True)
          return JsonResponse({'status': 'success', 'result': suppliersData.data, 'page': data['page']}, safe=False)
        except:
          return JsonResponse({'status': 'not-found'})
        

@csrf_exempt
def printSupplierById(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        supplier = Supplier.objects.filter(supplier_id=data['supplier_id'])
        supplierData = SupplierSerializer(supplier, many=True)
        return JsonResponse({'status': 'success', 'result': supplierData.data}, safe=False)

@csrf_exempt
def printSuppliersBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        suppliers = Supplier.objects.filter(Q(supplier_name__icontains=term)|
                   Q(state__icontains=term)|Q(supplier_id__iexact=term)|
                   Q(mobile__icontains=term)|Q(city__icontains=term)
                   |Q(gstin__icontains=term)).order_by('-supplier_id')
        suppliersData = SupplierSerializer(suppliers, many=True)
        return JsonResponse({'status': 'success', 'result': suppliersData.data}, safe=False)           


@csrf_exempt
def updateSupplier(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        Supplier.objects.filter(supplier_id=data['supplier_id']).update(supplier_name=data['supplierName'], mobile=data['mobile'],
                            whatsappNo=data['whatsapp'], email=data['email'], address=data['address'],
                            city=data['city'], state=data['state'], pincode=data['pincode'], gstin=data['gstin'],
                            openingBalance=data['openingBalance'], salesDues=data['salesDues'], returnDues=data['returnDues'])
        return JsonResponse({'status': 'updated'}, safe=False)

@csrf_exempt
def deleteSuppliers(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Supplier.objects.filter(supplier_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Supplier handling ends


# Purchase handling starts
@csrf_exempt
def createPurchase(request):
  if request.method == "POST":
      data = JSONParser().parse(request)
      supplier_id = data['supplier']
      items = json.loads(data['items'])
      for item in items:
          itemData = Item.objects.get(item_id=item['item_id'])
          itemData.stock_qty = int(itemData.stock_qty) + int(item['group_unit_qty'])
          itemData.save()
      if supplier_id.isnumeric():
       # Recalculating with of supplier
       if Supplier.objects.filter(supplier_id=supplier_id).exists:
          supplier = Supplier.objects.get(supplier_id=supplier_id)
          supplier.salesDues = Decimal(data['remainingAmount'])
          supplier.openingBalance = Decimal(0)
          supplier.returnDues = Decimal(0)
          supplier.save()
       # Making all previous purchases paid
       if Purchase.objects.filter(supplier_id=supplier_id).exists():
          purchases = Purchase.objects.filter(supplier_id=supplier_id)
          for i in purchases:
              i.status = "Paid" 
              i.paid_amount =  i.grand_total
              i.due_amount = 00.00
              i.save()
      purchase = Purchase(supplier_id=supplier_id,supplier_name=data['supplierName'],
                     gstin=data['gstin'],mobile=data['mobile'],city=data['city'],
                     state=data['state'],pincode=data['pincode'],address=data['address'],
                     purchase_no=data['purchaseNo'],issue_date=data['issueDate'],
                     supply=data['supply'], items=data['items'], discount_type=data['discountType'],
                     discount_value=data['discountOnAll'],shipping_charges=data['shippingCharges'],
                     paid_amount=data['paidAmount'], due_amount=data['remainingAmount'],
                     pay_mode=data['payMode'],pay_note=data['paymentNote'], 
                     whatsapp_no=data['whatsappNo'],
                     tax_rate=data['taxRate'],sub_total=Decimal(data['subTotal']), tax_amount=Decimal(data['taxAmount']), 
                     grand_total=Decimal(data['grandTotal']), item_total=Decimal(data['itemTotal']))     
      if data['dueDate']:
          purchase.due_date = data['dueDate']                 
      if Decimal(data['paidAmount'])==0:
          purchase.status = "Unpaid"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])>0:
          purchase.status = "Due"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])==0:
          purchase.status = "Paid"            
      purchase.save()               
      return JsonResponse({'status': 'success', 'purchase_id': purchase.purchase_id, 'whatsapp': purchase.whatsapp_no}, safe=False) 

@csrf_exempt
def savePurchaseFile(request):
    if request.method == "POST":
        purchase_file = request.FILES.get('purchaseFile')
        purchase_id = request.POST.get('purchase_id')
        whatsapp_no = request.POST.get('whatsapp')
        purchaseFile.objects.create(purchase_file=purchase_file, purchase_id=purchase_id, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})

@csrf_exempt
def printFileById(request):
  if request.method == "POST":
      data = JSONParser().parse(request)
      bill = purchaseFile.objects.filter(purchase_id=data['purchase_id'])
      billData = PurchaseFileSerializer(bill, many=True)
      return JsonResponse({'status': 'success', 'result': billData.data}, safe=False)

@csrf_exempt
def updateFile(request):
    if request.method == "POST":
        purchase_file = request.FILES.get('purchaseFile')
        purchase_id = request.POST.get('purchase_id')
        whatsapp_no = request.POST.get('whatsapp')
        purchaseFile.objects.filter(purchase_id=purchase_id).delete()
        purchaseFile.objects.create(purchase_id=purchase_id,purchase_file=purchase_file, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})


@csrf_exempt
def updatePurchase(request):
 if request.method == "POST":
      data = JSONParser().parse(request)
      purchase = Purchase.objects.get(purchase_id=data['purchase_id'])
      supplier_id = data['supplier']
      items = json.loads(data['items'])
      purchaseItems = json.loads(data['items'])  
      if len(items) != len(purchaseItems):
        for item in items:
          itemData = Item.objects.get(item_id=item['item_id'])
          itemData.stock_qty = int(itemData.stock_qty) - int(item['group_unit_qty'])
          itemData.save()
      if supplier_id.isnumeric():
       # Recalculating dues with supplier
       if Supplier.objects.filter(supplier_id=supplier_id).exists:
          supplier = Supplier.objects.get(supplier_id=supplier_id)
          supplier.salesDues = Decimal(data['remainingAmount'])
          supplier.openingBalance = Decimal(0)
          supplier.returnDues = Decimal(0)
          supplier.save()
      purchase.paid_amount = purchase.paid_amount + data['paidAmount']
      purchase.due_amount = data['remainingAmount']    
      if data['discountOnAll']:
          purchase.discount_value=data['discountOnAll']
      if data['discountType'] and data['discountOnAll']:
          purchase.discount_type=data['discountType']
      if data['shippingCharges']:
          purchase.shipping_charges = data['shippingCharges']
      if data['dueDate']:
          purchase.due_date = data['dueDate']         
      if Decimal(data['paidAmount'])==0:
          purchase.status = "Unpaid"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])>0:
          purchase.status = "Due"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])==0:
          purchase.status = "Paid"      
          purchase.due_amount = 0
      purchase.save()     
      Purchase.objects.filter(purchase_id=data['purchase_id']).update(supplier_id=supplier_id,supplier_name=data['supplierName'],
                     gstin=data['gstin'],mobile=data['mobile'],city=data['city'],
                     state=data['state'],pincode=data['pincode'],address=data['address'],
                     purchase_no=data['purchaseNo'],issue_date=data['issueDate'], supply=data['supply'], 
                     items=data['items'], due_amount=data['remainingAmount'],
                     pay_mode=data['payMode'],pay_note=data['paymentNote'], 
                     tax_rate=data['taxRate'],sub_total=Decimal(data['subTotal']), tax_amount=Decimal(data['taxAmount']), 
                     grand_total=Decimal(data['grandTotal']), item_total=Decimal(data['itemTotal']) )                 
      return JsonResponse({'status': 'success', 'purchase_id': purchase.purchase_id, 'whatsapp': purchase.whatsapp_no}, safe=False) 

@csrf_exempt
def getReturnPurchase(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        purchase = Purchase.objects.get(purchase_id=data['purchase_id'])
        if purchase.status!='Returned':
          if purchase.supplier_id.isnumeric():
           if Supplier.objects.filter(supplier_id=purchase.supplier_id).exists():
            supplier = Supplier.objects.get(supplier_id=purchase.supplier_id)
            returnableAmount = purchase.item_total
            return JsonResponse({'status': 'success', 'returnableAmount': returnableAmount, 
            'purchase_no': purchase.purchase_no, 'supplier': purchase.supplier_id}, safe=False)
           elif not Supplier.objects.filter(supplier_id=supplier_id).exists():    
            return JsonResponse({'status': 'not-found'})
          elif purchase.supplier_id=='Walk-in Customer':
            return JsonResponse({'status': 'success', 'returnableAmount': purchase.item_total, 
            'purchase_no': purchase.purchase_no, 'supplier': 'walk'}, safe=False)
        else:
            return JsonResponse({'status': 'returned'}, safe=False)    

@csrf_exempt
def returnPurchase(request):
    if request.method == "POST":
       data = JSONParser().parse(request)
       purchase = Purchase.objects.get(purchase_id=data['purchase_id'])
       purchase.status='Returned'
       purchase.due_amount = 0
       purchase.paid_amount = 0
       purchase.save()
       try:
           supplier = Supplier.objects.get(supplier_id=data['supplier'])
           balance = Decimal(supplier.openingBalance) + Decimal(supplier.salesDues) - Decimal(supplier.returnDues) - Decimal(data['amountLeft'])
           if balance>=0:
               supplier.openingBalance = balance
               supplier.salesDues = 0
               supplier.returnableAmount = 0
           elif balance<0:
                supplier.returnDues =  - balance
                supplier.openingBalance = 0
                supplier.salesDues = 0
           supplier.save()
       except:
            pass
       return JsonResponse({'status': 'success'})


@csrf_exempt
def printPurchases(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        purchases = Purchase.objects.all().order_by('-purchase_id')
        p = Paginator(purchases,10)
        try:
          purchases = p.page(data['page'])
          purchasesData = PurchaseSerializer(purchases, many=True)
          return JsonResponse({'status': 'success', 'result': purchasesData.data, 'page':data['page']}, safe=False)
        except:
             return JsonResponse({'status': 'not-found'})

@csrf_exempt
def printPurchasesBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        purchases = Purchase.objects.filter(Q(purchase_no__icontains=term)|
                   Q(supplier_name__icontains=term)|Q(supplier_id__iexact=term)|
                   Q(status__icontains=term)).order_by('-purchase_id')
        purchasesData = PurchaseSerializer(purchases, many=True)
        return JsonResponse({'status': 'success', 'result': purchasesData.data}, safe=False)           

@csrf_exempt
def printPurchaseById(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        purchase = Purchase.objects.filter(purchase_id=data['purchase_id'])
        purchaseData = PurchaseSerializer(purchase, many=True)
        return JsonResponse({'status': 'success', 'result': purchaseData.data}, safe=False)

@csrf_exempt
def deletePurchases(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Purchase.objects.filter(purchase_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)
# Purchase handling ends
