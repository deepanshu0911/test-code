from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q
from django.core.paginator import Paginator
from selling.models import Item, Client, Invoice, Quotation, billFile, quoteFile
from selling.serializers import ItemSerializer, ClientSerializer, InvoiceSerializer, QuotationSerializer, BillSerializer, QuoteFileSerializer
from decimal import Decimal
import json

# Client handling starts
@csrf_exempt
def createClient(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if not Client.objects.filter(client_name=data['clientName']).exists():
            Client.objects.create(client_name=data['clientName'], mobile=data['mobile'],
                            whatsappNo=data['whatsapp'], email=data['email'], address=data['address'],
                            city=data['city'], state=data['state'], pincode=data['pincode'], gstin=data['gstin'])
            return JsonResponse({'status': 'created'}, safe=False)
        else: 
            return JsonResponse({'status': 'exists'}, safe=False)   

@csrf_exempt
def printClients(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        clients = Client.objects.all().order_by('-client_id')
        p = Paginator(clients,10)
        try:
          clients = p.page(data['page'])
          clientsData = ClientSerializer(clients, many=True)
          return JsonResponse({'status': 'success', 'result': clientsData.data, 'page': data['page']}, safe=False)
        except:
          return JsonResponse({'status': 'not-found'})
        
@csrf_exempt
def printClientById(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        client = Client.objects.filter(client_id=data['client_id'])
        clientsData = ClientSerializer(client, many=True)
        return JsonResponse({'status': 'success', 'result': clientsData.data}, safe=False)

@csrf_exempt
def printClientsBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        clients =  Client.objects.filter(Q(city__icontains=term)|
                   Q(client_name__icontains=term)|Q(client_id__iexact=term)|
                   Q(state__icontains=term)|Q(gstin__icontains=term)|
                   Q(mobile__icontains=term)).order_by('-client_id')
        clientsData = ClientSerializer(clients, many=True)
        return JsonResponse({'status': 'success', 'result': clientsData.data}, safe=False)           
    

@csrf_exempt
def updateClient(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        Client.objects.filter(client_id=data['client_id']).update(client_name=data['clientName'], mobile=data['mobile'],
                            whatsappNo=data['whatsapp'], email=data['email'], address=data['address'],
                            city=data['city'], state=data['state'], pincode=data['pincode'], gstin=data['gstin'],
                            openingBalance=data['openingBalance'], salesDues=data['salesDues'], returnDues=data['returnDues'])
        return JsonResponse({'status': 'updated'}, safe=False)

@csrf_exempt
def deleteClients(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Client.objects.filter(client_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Client handling ends

# Item handling starts
@csrf_exempt
def createItem(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        lastItem = Item.objects.all().order_by('-item_id')[:1]
        if lastItem:
           code = 'IT0' + str(int(lastItem[0].item_id)+1)
        else:
            code = 'IT00'  
        hsn = ''
        sku = ''
        if data['hsn']:
            hsn = data['hsn'].upper()
        if data['sku']:
            sku = data['sku'].upper()           
        if not Item.objects.filter(item_code=code).exists():
            Item.objects.create(item_code=code, item_name=data['name'], stock_qty=data['qty'],unit=data['unit'], 
                             group_unit_qty=data['groupUnit'], tax_rate=data['tax'], tax_type=data['taxType'], 
                             cost_price=data['costPrice'], purchased_price=data['purchasedPrice'], profit_margin=data['margin'],
                              sales_price=data['salesPrice'], final_price=data['finalPrice'], note=data['note'],
                             unit_price=data['unitPrice'], tax_amount=data['taxAmount'])
            return JsonResponse({'status': 'created'}, safe=False)

@csrf_exempt
def printItems(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        items = Item.objects.all().order_by('-item_id')
        p = Paginator(items,10)
        try:
          items = p.page(data['page'])
          itemsData = ItemSerializer(items, many=True)
          return JsonResponse({'status': 'success', 'result': itemsData.data, 'page':data['page']}, safe=False)
        except:
           return JsonResponse({'status': 'not-found'})

@csrf_exempt
def printItemsBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        items = Item.objects.filter(Q(item_code__icontains=term)|
                   Q(item_name__icontains=term)|Q(item_id__iexact=term)|
                   Q(description__icontains=term)).order_by('-item_id')
        itemsData = ItemSerializer(items, many=True)
        return JsonResponse({'status': 'success', 'result': itemsData.data}, safe=False)           


@csrf_exempt
def printItemById(request):
   if request.method == "POST":
        data = JSONParser().parse(request)
        item = Item.objects.filter(item_id=data['item_id'])
        itemsData = ItemSerializer(item, many=True)
        return JsonResponse({'status': 'success', 'result': itemsData.data}, safe=False)
      
@csrf_exempt
def searchItem(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        code = data['itemCode']
        if Item.objects.filter(item_code__iexact=code).exists():
            item = Item.objects.filter(item_code__iexact=code)
            itemData = ItemSerializer(item, many=True)
            return JsonResponse({'status': 'success', 'result': itemData.data}, safe=False)
        else:
            return JsonResponse({'status': 'not-found'}, safe=False)    

def searchingItem(request, search):
    if request.method=="GET":
      term = search
      if term!='' and term:
          item = Item.objects.filter(Q(item_code__icontains=term)|
          Q(item_name__icontains=term)).order_by('-item_id')[:10]
          itemData = ItemSerializer(item, many=True)
          return JsonResponse({'status': 'success', 'result': itemData.data}, safe=False)

@csrf_exempt
def updateItem(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        if Item.objects.filter(item_id=data['item_id']).exists():
            hsn = ''
            sku = ''
            if data['hsn']:
                hsn = data['hsn'].upper()
            if data['sku']:
                sku = data['sku'].upper()    
            Item.objects.filter(item_id=data['item_id']).update(item_code=data['code'], item_name=data['name'], 
                              hsn=hsn, sku=sku, stock_qty=data['qty'], unit=data['unit'],
                             group_unit_qty=data['groupUnit'], tax_rate=data['tax'], tax_type=data['taxType'], 
                             cost_price=data['costPrice'], purchased_price=data['purchasedPrice'], profit_margin=data['margin'],
                              sales_price=data['salesPrice'], final_price=data['finalPrice'], note=data['note'],
                             unit_price=data['unitPrice'], tax_amount=data['taxAmount'])
            return JsonResponse({'status': 'updated'}, safe=False)

@csrf_exempt
def deleteItems(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Item.objects.filter(item_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Item handling ends


# Invoice handling starts
@csrf_exempt
def createInvoice(request):
  if request.method == "POST":
      data = JSONParser().parse(request)  
      client_id = data['client']
      items = json.loads(data['items'])
      for item in items:
          itemData = Item.objects.get(item_id=item['item_id'])
          itemData.stock_qty = int(itemData.stock_qty) - int(item['group_unit_qty'])
          itemData.qty_sold = int(itemData.qty_sold) + int(item['group_unit_qty'])
          itemData.save()
      if client_id.isnumeric():
       # Recalculating dues of client
       if Client.objects.filter(client_id=client_id).exists:
          client = Client.objects.get(client_id=client_id)
          client.salesDues = Decimal(data['remainingAmount'])
          client.openingBalance = Decimal(0)
          client.returnDues = Decimal(0)
          client.save()
       # Making all previous invoice paid
       if Invoice.objects.filter(client_id=client_id).exists():
          invoices = Invoice.objects.filter(client_id=client_id)
          for i in invoices:
              i.status = "Paid" 
              i.paid_amount =  i.grand_total
              i.due_amount = 00.00
              i.save()
      invoice = Invoice(client_id=client_id,client_name=data['clientName'],
                     gstin=data['gstin'],mobile=data['mobile'],city=data['city'],
                     state=data['state'],pincode=data['pincode'],address=data['address'],
                     invoice_no=data['invoiceNo'],issue_date=data['issueDate'], supply=data['supply'], 
                     items=data['items'], discount_type=data['discountType'],
                     discount_value=data['discountOnAll'],shipping_charges=data['shippingCharges'],
                     paid_amount=data['paidAmount'], due_amount=data['remainingAmount'],
                     pay_mode=data['payMode'],pay_note=data['paymentNote'], whatsapp_no=data['whatsappNo'],
                     tax_rate=data['taxRate'],sub_total=Decimal(data['subTotal']), tax_amount=Decimal(data['taxAmount']),
                     grand_total=Decimal(data['grandTotal']), item_total=Decimal(data['itemTotal']) )  
      if data['dueDate']:
          invoice.due_date = data['dueDate']                
      if client_id=="Walk-in Customer":
          invoice.client_name = client_id
      if client_id=="Walk-in Customer" and data['clientName']!='':
          invoice.walk_in_client_name = data['clientName']
      if Decimal(data['paidAmount'])==0:
          invoice.status = "Unpaid"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])>0:
          invoice.status = "Due"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])==0:
          invoice.status = "Paid"            
      invoice.save()               
      return JsonResponse({'status': 'success', 'invoice_id': invoice.invoice_id, 'whatsapp': invoice.whatsapp_no}, safe=False) 

@csrf_exempt
def saveBillFile(request):
    if request.method == "POST":
        bill_file = request.FILES.get('billFile')
        invoice_id = request.POST.get('invoice_id')
        whatsapp_no = request.POST.get('whatsapp')
        billFile.objects.create(bill_file=bill_file, invoice_id=invoice_id, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})

@csrf_exempt
def printBillById(request):
  if request.method == "POST":
      data = JSONParser().parse(request)
      bill = billFile.objects.filter(invoice_id=data['invoice_id'])
      billData = BillSerializer(bill, many=True)
      return JsonResponse({'status': 'success', 'result': billData.data}, safe=False)

@csrf_exempt
def updateBillFile(request):
    if request.method == "POST":
        bill_file = request.FILES.get('billFile')
        invoice_id = request.POST.get('invoice_id')
        whatsapp_no = request.POST.get('whatsapp')
        billFile.objects.filter(invoice_id=invoice_id).delete()
        billFile.objects.create(invoice_id=invoice_id,bill_file=bill_file, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})

@csrf_exempt
def updateInvoice(request):
 if request.method == "POST":
      data = JSONParser().parse(request)
      invoice = Invoice.objects.get(invoice_id=data['invoice_id'])
      client_id = data['client']
      items = json.loads(data['items'])
      invoiceItems = json.loads(data['items'])  
      if len(items) != len(invoiceItems):
        for item in items:
          itemData = Item.objects.get(item_id=item['item_id'])
          itemData.stock_qty = int(itemData.stock_qty) - int(item['group_unit_qty'])
          itemData.qty_sold = int(itemData.qty_sold) + int(item['group_unit_qty'])
          itemData.save()
      if client_id.isnumeric():
       # Recalculating dues of client
       if Client.objects.filter(client_id=client_id).exists:
          client = Client.objects.get(client_id=client_id)
          client.salesDues = Decimal(data['remainingAmount'])
          client.openingBalance = Decimal(0)
          client.returnDues = Decimal(0)
          client.save()
      invoice.paid_amount = invoice.paid_amount + data['paidAmount']
      invoice.due_amount = data['remainingAmount'] 
      if data['discountOnAll']:
          invoice.discount_value=data['discountOnAll']
      if data['discountType'] and data['discountOnAll']:
          invoice.discount_type=data['discountType']
      if data['shippingCharges']:
          invoice.shipping_charges = data['shippingCharges']
      if data['dueDate']:
          invoice.due_date = data['dueDate']         
      if client_id=="Walk-in Customer":
          invoice.client_name = client_id
      if client_id=="Walk-in Customer" and data['clientName']!='':
          invoice.walk_in_client_name = data['clientName']
      if Decimal(data['paidAmount'])==0:
          invoice.status = "Unpaid"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])>0:
          invoice.status = "Due"
      if Decimal(data['paidAmount'])>0 and Decimal(data['remainingAmount'])==0:
          invoice.status = "Paid"     
          invoice.due_amount = 0   
    #   Calculating paid amount
     
      invoice.save()        
      Invoice.objects.filter(invoice_id=data['invoice_id']).update(client_id=client_id,client_name=data['clientName'],
                     gstin=data['gstin'],mobile=data['mobile'],city=data['city'],
                     state=data['state'],pincode=data['pincode'],address=data['address'],
                     invoice_no=data['invoiceNo'],issue_date=data['issueDate'],supply=data['supply'], 
                     items=data['items'], due_amount=data['remainingAmount'], pay_mode=data['payMode'],pay_note=data['paymentNote'], whatsapp_no=data['whatsappNo'],
                     tax_rate=data['taxRate'],sub_total=Decimal(data['subTotal']), tax_amount=Decimal(data['taxAmount']), 
                     grand_total=Decimal(data['grandTotal']), item_total=Decimal(data['itemTotal']))  
      return JsonResponse({'status': 'success', 'invoice_id': invoice.invoice_id, 'whatsapp': invoice.whatsapp_no}, safe=False) 

@csrf_exempt
def getReturnInvoice(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        invoice = Invoice.objects.get(invoice_id=data['invoice_id'])
        if invoice.status!='Returned':
          if invoice.client_id.isnumeric():
           if Client.objects.filter(client_id=invoice.client_id).exists():
            client = Client.objects.get(client_id=invoice.client_id)
            # returnableAmount = Decimal(invoice.grand_total) - Decimal(client.salesDues) - Decimal(client.openingBalance) + Decimal(client.returnDues)
            # returnableAmount = invoice.item_total - Decimal(client.salesDues) - Decimal(client.openingBalance) + Decimal(client.returnDues)
            returnableAmount = invoice.item_total
            return JsonResponse({'status': 'success', 'returnableAmount': returnableAmount, 
            'invoice_no': invoice.invoice_no, 'client': invoice.client_id}, safe=False)
           elif not Client.objects.filter(client_id=client_id).exists():    
            return JsonResponse({'status': 'not-found'})
          elif invoice.client_id=='Walk-in Customer':
            return JsonResponse({'status': 'success', 'returnableAmount': invoice.item_total, 
            'invoice_no': invoice.invoice_no, 'client': 'walk'}, safe=False)
        else:
            return JsonResponse({'status': 'returned'}, safe=False)    

@csrf_exempt
def returnInvoice(request):
    if request.method == "POST":
       data = JSONParser().parse(request)
       invoice = Invoice.objects.get(invoice_id=data['invoice_id'])
       invoice.status='Returned'
       invoice.due_amount = 0
       invoice.paid_amount = 0
       invoice.save()
       try:
           client = Client.objects.get(client_id=data['client'])
        #    client.returnDues = Decimal(client.returnDues) + Decimal(data['amountLeft'])
        #    if client.returnDues<0:
        #        client.openingBalance = - Decimal(client.returnDues)
        #        client.returnDues = 0
        #        client.salesDues = 0
           balance = Decimal(client.openingBalance)+ Decimal(client.salesDues) - Decimal(client.returnDues) - Decimal(data['amountLeft'])
           if balance>=0:
               client.openingBalance = balance
               client.salesDues = 0
               client.returnableAmount = 0
           elif balance<0:
                client.returnDues =  - balance
                client.openingBalance = 0
                client.salesDues = 0
           client.save()
       except:
            pass
       return JsonResponse({'status': 'success'})


@csrf_exempt
def printInvoices(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        invoices = Invoice.objects.all().order_by('-invoice_id')
        p = Paginator(invoices,10)
        try:
          invoices = p.page(data['page'])
          invoicesData = InvoiceSerializer(invoices, many=True)
          return JsonResponse({'status': 'success', 'result': invoicesData.data, 'page':data['page']}, safe=False)
        except:
             return JsonResponse({'status': 'not-found'})

@csrf_exempt
def printInvoicesBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        invoices = Invoice.objects.filter(Q(invoice_no__icontains=term)|
                   Q(client_name__icontains=term)|Q(client_id__iexact=term)|
                   Q(status__icontains=term)).order_by('-invoice_id')
        invoicesData = InvoiceSerializer(invoices, many=True)
        return JsonResponse({'status': 'success', 'result': invoicesData.data}, safe=False)           

@csrf_exempt
def printInvoiceById(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        invoice = Invoice.objects.filter(invoice_id=data['invoice_id'])
        invoiceData = InvoiceSerializer(invoice, many=True)
        return JsonResponse({'status': 'success', 'result': invoiceData.data}, safe=False)

@csrf_exempt
def deleteInvoices(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Invoice.objects.filter(invoice_id=i).delete()
            billFile.objects.filter(invoice_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)

# Invoice handling ends

# Quotation handling starts
@csrf_exempt
def createQuotation(request):
      data = JSONParser().parse(request)
      client_id = data['client']
      items = json.loads(data['items'])
      quotation = Quotation(client_id=client_id,client_name=data['clientName'],
                     gstin=data['gstin'],mobile=data['mobile'],city=data['city'],
                     state=data['state'],pincode=data['pincode'],address=data['address'],
                     quotation_no=data['quotationNo'],issue_date=data['issueDate'],supply=data['supply'], 
                     items=data['items'], discount_type=data['discountType'], discount_value=data['discountOnAll'],
                     shipping_charges=data['shippingCharges'], whatsapp_no=data['whatsappNo'],
                     tax_rate=data['taxRate'],sub_total=Decimal(data['subTotal']), 
                     tax_amount=Decimal(data['taxAmount']), grand_total=Decimal(data['grandTotal']) )       
      if client_id=="Walk-in Customer":
          quotation.client_name = client_id
      if client_id=="Walk-in Customer" and data['clientName']!='':
          quotation.walk_in_client_name = data['clientName']
      quotation.save()               
      return JsonResponse({'status': 'success', 'quotation_id': quotation.quotation_id, 'whatsapp': quotation.whatsapp_no}, safe=False) 
 
@csrf_exempt
def saveQuoteFile(request):
    if request.method == "POST":
        quote_file = request.FILES.get('quoteFile')
        quotation_id = request.POST.get('quotation_id')
        whatsapp_no = request.POST.get('whatsapp')
        quoteFile.objects.create(quote_file=quote_file, quotation_id=quotation_id, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})

@csrf_exempt
def printQuoteFileById(request):
  if request.method == "POST":
      data = JSONParser().parse(request)
      bill = quoteFile.objects.filter(quotation_id=data['quotation_id'])
      billData = QuoteFileSerializer(bill, many=True)
      return JsonResponse({'status': 'success', 'result': billData.data}, safe=False)

@csrf_exempt
def updateQuoteFile(request):
    if request.method == "POST":
        quote_file = request.FILES.get('quoteFile')
        quotation_id = request.POST.get('quotation_id')
        whatsapp_no = request.POST.get('whatsapp')
        quoteFile.objects.filter(quotation_id=quotation_id).delete()
        quoteFile.objects.create(quotation_id=quotation_id,quote_file=quote_file, whatsappNo=whatsapp_no)
        return JsonResponse({'status': 'success'})

@csrf_exempt
def printQuotations(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        quotations = Quotation.objects.all().order_by('-quotation_id')
        p = Paginator(quotations,10)
        try:
          quotations = p.page(data['page'])
          quotationsData = QuotationSerializer(quotations, many=True)
          return JsonResponse({'status': 'success', 'result': quotationsData.data, 'page': data['page']}, safe=False)
        except:
          return JsonResponse({'status': 'not-found'})     

@csrf_exempt
def printQuotationsBySearch(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        term = data['term']
        quotations = Quotation.objects.filter(Q(client_name__icontains=term)|
                   Q(quotation_no__icontains=term)|Q(quotation_id__iexact=term)|
                   Q(city__icontains=term)).order_by('-quotation_id')
        quotationsData = QuotationSerializer(quotations, many=True)
        return JsonResponse({'status': 'success', 'result': quotationsData.data}, safe=False)           


@csrf_exempt
def deleteQuotations(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        selectedIds = data['selectedIds']
        for i in selectedIds:
            Quotation.objects.filter(quotation_id=i).delete()
        return JsonResponse({'status': 'success'}, safe=False)          

# Quotation handling ends