from django.db import models
import uuid
import os


def featured_item_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/item_images', filename)

def bill_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/invoices', filename)


def quote_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/quotations', filename)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=10, null=True, blank=True)
    item_name = models.CharField(max_length=100)
    description = models.TextField(default='-')
    hsn = models.CharField(max_length=50, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    group_unit = models.CharField(max_length=50, null=True, blank=True)
    group_unit_qty = models.IntegerField(default=1)
    stock_qty = models.IntegerField(null=True, blank=True)
    alert_qty = models.IntegerField(null=True, blank=True, default=10)
    tax_name = models.CharField(max_length=50, null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=1,null=True, blank=True)
    cost_price = models.CharField(max_length=50, null=True, blank=True)
    purchased_price = models.CharField(max_length=50, null=True, blank=True)
    tax_type = models.CharField(max_length=50, null=True, blank=True)
    profit_margin = models.CharField(max_length=50,null=True, blank=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    unit_price =  models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True) 
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    qty_sold = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.item_code + '-' + self.item_name
    
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    mobile = models.IntegerField(null=True, blank=True)
    whatsappNo = models.CharField(max_length=20,null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)    
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    gstin = models.CharField(max_length=20, null=True, blank=True)
    openingBalance = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    # salesDues = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    salesDues = models.CharField(max_length=50, null=True, blank=True)
    returnDues = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.client_name

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    
    # Client details
    client_id = models.CharField(max_length=50,null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    walk_in_client_name = models.CharField(max_length=50, null=True, blank=True)
    gstin = models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    invoice_no = models.CharField(max_length=50, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    pay_terms = models.CharField(max_length=50,null=True, blank=True) 
    supply = models.CharField(max_length=50, null=True, blank=True)
    items = models.TextField(null=True, blank=True)
    discount_type = models.CharField(max_length=50, null=True, blank=True)
    discount_value = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    shipping_charges = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    tax_rate = models.CharField(max_length=50, null=True, blank=True)
    item_total = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    due_amount = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    pay_mode = models.CharField(max_length=50, null=True, blank=True)
    pay_note = models.TextField(null=True, blank=True)
    whatsapp_no = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=50, default="Paid")
    bill_file = models.FileField(upload_to=bill_image, null=True, blank=True)

    created_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.invoice_no + ' - ' + self.client_name

class Quotation(models.Model):
    quotation_id = models.AutoField(primary_key=True)
    quotation_no = models.CharField(max_length=50, null=True, blank=True)

    # Client details
    client_id = models.CharField(max_length=50,null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    walk_in_client_name = models.CharField(max_length=50, null=True, blank=True)
    gstin = models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    issue_date = models.DateField(null=True, blank=True)
    supply = models.CharField(max_length=50, null=True, blank=True)
    items = models.TextField(null=True, blank=True)
    discount_type = models.CharField(max_length=50, null=True, blank=True)
    discount_value = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    shipping_charges = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    tax_rate = models.CharField(max_length=50, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    whatsapp_no = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=50, default="Paid")
    bill_file = models.TextField(null=True, blank=True)

    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.quotation_no + ' - ' + self.client_name 

    

class billFile(models.Model):
    invoice_id = models.IntegerField(null=True, blank=True)
    bill_file = models.FileField(upload_to=bill_image, null=True, blank=True)
    whatsappNo = models.CharField(max_length=20, null=True, blank=True)   
    
    def delete(self, *args, **kwargs):
        # first, delete the file
        self.bill_file.delete(save=False)

        # now, delete the object
        super(billFile, self).delete(*args, **kwargs)

class quoteFile(models.Model):
    quotation_id = models.IntegerField(null=True, blank=True)
    quote_file = models.FileField(upload_to=quote_image, null=True, blank=True)
    whatsappNo = models.CharField(max_length=20, null=True, blank=True)   
    
    def delete(self, *args, **kwargs):
        # first, delete the file
        self.quote_file.delete(save=False)

        # now, delete the object
        super(quoteFile, self).delete(*args, **kwargs)