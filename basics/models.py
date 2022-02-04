from django.db import models
import uuid
import os

class CompanyProfile(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    mobile2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    gstin = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    created = models.CharField(max_length=50, default="already")
    profile_pic = models.FileField(default='uploads/store_profile/FK.png')
    objects = models.Manager()

    def __str__(self):
        return self.company_name

class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=50) 
    tax_rate = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.tax_name

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=50) 
    # unit_qty = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    unit_qty = models.IntegerField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.unit_name
        
class Help(models.Model):
    help_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    solution = models.TextField(default="Waiting for solution. Usually takes 1 day.")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
     return str(self.help_id)        
    


    
  
    

