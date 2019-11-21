from rest_framework import serializers
from .models import Borrower, Loan, Address, Payment

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['borrower_name', 'contact_name', 'contact_email_address', 'contact_work_telephone', 'contact_mobile_telephone']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['line_1', 'line_2', 'city', 'us_state', 'zipcode']

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['loan_type', 'payment_frequency', 'loan_origination_amount', 'loan_convention', 'loan_interest_rate', 'loan_term', 'date_loan_funded', 'loan_settlement_date', 'loan_maturity_date']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_amount', 'payment_date']