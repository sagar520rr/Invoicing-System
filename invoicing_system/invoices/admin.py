from django.contrib import admin
from .models import Invoice, Expense, Product, Transaction, BalanceSheet, IncomeStatement, CashFlowStatement

admin.site.register(Invoice)
admin.site.register(Expense)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(BalanceSheet)
admin.site.register(IncomeStatement)
admin.site.register(CashFlowStatement)

