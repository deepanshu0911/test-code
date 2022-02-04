from rest_framework import serializers
from management.models import Expense, Supplier, Purchase, purchaseFile

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('expense_id', 'expense_no', 'category', 'expense_for', 
                 'amount', 'note', 'expense_date', 'created_date')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('supplier_id', 'supplier_name', 'mobile', 'whatsappNo',
                  'email', 'address', 'city', 'state', 'pincode', 'gstin',
                  'openingBalance', 'salesDues', 'returnDues', 'created_date',
                  'last_updated')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('purchase_id', 'purchase_no', 'supplier_id', 'supplier_name', 'gstin',
                 'mobile', 'city', 'state', 'pincode', 'address', 'issue_date', 'due_date',
                 'supply', 'items', 'discount_type', 'discount_value', 'shipping_charges',
                 'sub_total', 'tax_amount', 'tax_rate', 'item_total', 'grand_total', 'paid_amount', 'due_amount',
                 'pay_mode', 'pay_note', 'whatsapp_no', 'status', 'bill_file', 'created_date')

class PurchaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = purchaseFile
        fields = ('id', 'purchase_id', 'purchase_file', 'whatsappNo')