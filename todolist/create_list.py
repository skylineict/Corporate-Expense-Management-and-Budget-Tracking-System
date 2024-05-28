from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework import permissions,authentication
from rest_framework.permissions import IsAuthenticated
from .serializer import TodolistSerializer
from .models import Todolist
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['POST'])
 # Add authentication classes here
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can access
def create_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class CreateTodoList(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TodolistSerializer
#     # authentication_classes  = [authentication.TokenAuthentication]

#     def perform_create(self, serializer):
#         return serializer.save(create_by=self.request.user)

class Listandcreateview(ListCreateAPIView):
    serializer_class = TodolistSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
      user = serializer.save(create_by=self.request.user)
      print(user)
      
      return user 
    

    def get_queryset(self):
       todolist = Todolist.objects.all()
       return todolist
    



