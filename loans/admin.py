
from django.contrib import admin
from . models import Borrower, Address, Loan, Payment

# Register your models here.

admin.site.register(Borrower)
admin.site.register(Address)
admin.site.register(Loan)
admin.site.register(Payment)