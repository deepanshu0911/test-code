from rest_framework import serializers
from selling.models import Item, Client, Invoice, Quotation, billFile, quoteFile

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'item_code', 'item_name', 'description', 'hsn', 'sku', 'unit',
                 'group_unit', 'group_unit_qty', 'stock_qty', 'alert_qty', 'cost_price',
                 'tax_name', 'tax_rate', 'purchased_price', 'tax_type', 'profit_margin',
                 'sales_price', 'final_price', 'note','created_date', 'unit_price', 'tax_amount', 'discount',
                 'qty_sold')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'client_name', 'mobile', 'whatsappNo',
                  'email', 'address', 'city', 'state', 'pincode', 'gstin',
                  'openingBalance', 'salesDues', 'returnDues', 'created_date',
                  'last_updated')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('invoice_id', 'invoice_no', 'client_id', 'client_name', 'walk_in_client_name', 'gstin',
                 'mobile', 'city', 'state', 'pincode', 'address', 'issue_date', 'due_date',
                 'pay_terms', 'supply', 'items', 'discount_type', 'discount_value', 'shipping_charges',
                 'sub_total', 'tax_amount', 'tax_rate', 'item_total', 'grand_total', 'paid_amount', 'due_amount',
                 'pay_mode', 'pay_note', 'whatsapp_no', 'bill_file', 'status', 'created_date')

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = billFile
        fields = ('id', 'invoice_id', 'bill_file', 'whatsappNo')

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = ('quotation_id', 'quotation_no', 'client_id', 'client_name', 'walk_in_client_name', 'gstin',
                 'mobile', 'city', 'state', 'pincode', 'address', 'issue_date', 'supply', 'items', 'discount_type', 
                 'discount_value', 'shipping_charges', 'sub_total', 'tax_amount', 'tax_rate', 'grand_total', 
                 'whatsapp_no', 'status', 'bill_file', 'created_date')

class QuoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = quoteFile
        fields = ('id', 'quotation_id', 'quote_file', 'whatsappNo')
