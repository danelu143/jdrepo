from django.contrib import admin
from testapp.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','Ceo','Location']

admin.site.register(Company,CompanyAdmin)
