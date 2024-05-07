from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import csv
# Create your views here.

def upload_transaction(request):
    return render(request, "transactions/index.html")

@api_view(['POST'])
def upload_csv(request):
    csv_file = request.FILES['file']
    if csv_file is not None:
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            Transaction.objects.create(
                amount=row['Amount'],
                status=row['Status'],
                invoice_url=row['InvoiceURL']
            )
        return Response({'message': 'CSV file uploaded successfully'})
    return Response({'error': 'No CSV file found'}, status=400)


@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'GET'])
def update_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    return Response({'message': 'Transaction deleted successfully'})


@api_view(['POST'])
def empty_database(request):
    Transaction.objects.all().delete()  # Delete all objects from the model
    return Response({'message': 'Database emptied successfully'})

