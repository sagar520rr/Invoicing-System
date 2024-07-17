from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    invoice_number = models.CharField(max_length=20, unique=True, default='INV-0001')
    invoice_date = models.DateField(default=timezone.now)  # Provide a default value
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer_name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.description

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)  # e.g., 'income', 'expense'

    def __str__(self):
        return f"{self.transaction_type} of ${self.amount} on {self.date}"

class BalanceSheet(models.Model):
    date = models.DateField()
    assets = models.DecimalField(max_digits=10, decimal_places=2)
    liabilities = models.DecimalField(max_digits=10, decimal_places=2)
    equity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Balance Sheet on {self.date}"

class IncomeStatement(models.Model):
    date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    net_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Income Statement on {self.date}"

class CashFlowStatement(models.Model):
    date = models.DateField()
    cash_inflows = models.DecimalField(max_digits=10, decimal_places=2)
    cash_outflows = models.DecimalField(max_digits=10, decimal_places=2)
    net_cash_flow = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cash Flow Statement on {self.date}"
