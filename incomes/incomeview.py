from rest_framework.views import APIView
from .incomserializer import IncomesSerilizers
from .models import  Income
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from expense.permission import IsOwner


class ListincomeView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
              request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','amount','source','description'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='name'),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='amount'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                'source': openapi.Schema(type=openapi.TYPE_STRING, description='source')
                
                }
        )


    )
  
    def post(self, request):
        serialier = IncomesSerilizers(data=request.data)
        if serialier.is_valid(raise_exception=True):
            serialier.save(created_by=request.user)
            return Response({"message": 'created successfully'}, status.HTTP_201_CREATED)
        
        return Response(serialier.errors)
        
   
    def get(self, request):
        income = Income.objects.filter(created_by=request.user)
        serializer = IncomesSerilizers(income, many=True)
        return Response(serializer.data)
    
    

class UpdateIncome(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomesSerilizers
    queryset = Income.objects.all()
    permission_classes = [IsOwner,IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

  


        
