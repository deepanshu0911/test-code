from rest_framework import serializers
from basics.models import CompanyProfile, Tax, Unit, Help

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('company_id', 'company_name', 'mobile', 'mobile2', 'email',
                  'address', 'city', 'state', 'pincode', 'gstin', 'website', 
                  'created_date', 'created', 'profile_pic' )

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ('tax_id', 'tax_name', 'tax_rate', 'created_date')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('unit_id', 'unit_name', 'unit_qty', 'created_date')

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('help_id', 'category', 'description', 'solution', 'created_date')
