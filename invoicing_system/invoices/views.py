from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Invoice, Product, Expense, Transaction, BalanceSheet, IncomeStatement, CashFlowStatement
from .serializers import (
    InvoiceSerializer,
    ProductSerializer,
    ExpenseSerializer,
    TransactionSerializer,
    BalanceSheetSerializer,
    IncomeStatementSerializer,
    CashFlowStatementSerializer,
)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Log serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class BalanceSheetViewSet(viewsets.ModelViewSet):
    queryset = BalanceSheet.objects.all()
    serializer_class = BalanceSheetSerializer

class IncomeStatementViewSet(viewsets.ModelViewSet):
    queryset = IncomeStatement.objects.all()
    serializer_class = IncomeStatementSerializer

class CashFlowStatementViewSet(viewsets.ModelViewSet):
    queryset = CashFlowStatement.objects.all()
    serializer_class = CashFlowStatementSerializer
