from django.db import models
from django.utils import timezone

# Create your models here.

class Borrower(models.Model):
    borrower_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=40) 
    contact_email_address = models.CharField(max_length=55)
    contact_work_telephone = models.CharField(max_length=30)
    contact_mobile_telephone = models.CharField(max_length=30, default=None)

    def __str__(self):
        return f"{self.borrower_name}"

class Address(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='addresses')
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255)
    us_state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.line_1}"


class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loans')
    loan_type = models.CharField(max_length=30)
    payment_frequency = models.CharField(max_length=30)
    loan_origination_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_convention = models.IntegerField()
    loan_interest_rate = models.DecimalField(max_digits=12, decimal_places=2)
    loan_term = models.DecimalField(max_digits=12, decimal_places=1)
    date_loan_funded = models.DateField()
    loan_settlement_date = models.DateField()
    loan_maturity_date = models.DateField()
  
    def __str__(self):
        return f"{self.loan_type} {self.loan_maturity_date}"

class Payment(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='payments')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.payment_amount} {self.payment_date}"