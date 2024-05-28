from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
# from .categoryserializer import CategorySerializer
from .permission import OnlyadminEdit,IsOwner
from .models import Category,Expenses
from .expensserializer import ExpensiveSerializer
from .pagnations import Pagninationsview







class ExpensVeiw(ListCreateAPIView):
    pagination_class = Pagninationsview
    serializer_class = ExpensiveSerializer
    queryset = Expenses.objects.all()
    permission_classes = [IsOwner,IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)



class ExpensesDatailsview(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensiveSerializer
    queryset = Expenses.objects.all()
    permission_classes =  permission_classes = [IsOwner,IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)







