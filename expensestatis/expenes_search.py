from expense.models import Expenses
from expense.expensserializer import ExpensiveSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .adminpermission import Adminonly
from rest_framework import status, response




class ExpensesSearchVeiw(ListAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensiveSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [Adminonly]
    filterset_fields = ['created_by__username','name']

    def get_queryset(self):
         return Expenses.objects.all()
    
    def list(self, request, *args, **kwargs):
         queryset = self.filter_queryset(self.get_queryset())
         if not queryset.exists():
            return response.Response({'message': 'Expense not found'}, status=status.HTTP_404_NOT_FOUND)
         serializer = self.get_serializer(queryset, many=True)
         return response.Response(serializer.data)
       
    
    
     
              
        
       



