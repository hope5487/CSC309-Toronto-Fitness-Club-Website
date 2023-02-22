from django.contrib import admin

# Register your models here.
from banks.models import Bank, Branch

admin.site.register(Bank)
admin.site.register(Branch)
