from django.db import models
import uuid
import os

def purchase_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/purchases', filename)

class Expense(models.Model):
   expense_id = models.AutoField(primary_key=True)
   expense_no = models.IntegerField(null=True, blank=True)
   category = models.CharField(max_length=50, null=True, blank=True)
   expense_for = models.CharField(max_length=100, null=True, blank=True)
   amount = models.CharField(max_length=50, null=True, blank=True)
   note = models.TextField(null=True, blank=True)
   expense_date = models.DateField(null=True, blank=True)
   created_date = models.DateField(auto_now_add=True)

   def __str__(self):
       return str(self.expense_no) + ' - ' +str(self.expense_for) 

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    mobile = models.IntegerField(null=True, blank=True)
    whatsappNo = models.CharField(max_length=20,null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)    
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    gstin = models.CharField(max_length=20, null=True, blank=True)
    openingBalance = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    salesDues = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    returnDues = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.supplier_name     

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    
    # Client details
    supplier_id = models.CharField(max_length=50,null=True, blank=True)
    supplier_name = models.CharField(max_length=50, null=True, blank=True)
    gstin = models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    purchase_no = models.CharField(max_length=50, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
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
    bill_file = models.TextField(null=True, blank=True)

    created_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.purchase_no + ' - ' + self.supplier_name


class purchaseFile(models.Model):
    purchase_id = models.IntegerField(null=True, blank=True)
    purchase_file = models.FileField(upload_to=purchase_image, null=True, blank=True)
    whatsappNo = models.CharField(max_length=20, null=True, blank=True)   
    
    def delete(self, *args, **kwargs):
        # first, delete the file
        self.purchase_file.delete(save=False)

        # now, delete the object
        super(purchaseFile, self).delete(*args, **kwargs)


