from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InvoiceViewSet,
    ProductViewSet,
    ExpenseViewSet,
    TransactionViewSet,
    BalanceSheetViewSet,
    IncomeStatementViewSet,
    CashFlowStatementViewSet,
)

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'products', ProductViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'balance_sheets', BalanceSheetViewSet)
router.register(r'income_statements', IncomeStatementViewSet)
router.register(r'cash_flow_statements', CashFlowStatementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
