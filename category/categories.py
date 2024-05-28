from .categoryserializer import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from expense.permission import OnlyadminEdit
from expense.pagnations import Pagninationsview
from rest_framework.parsers import MultiPartParser, FormParser
from expense.models import Category




class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [OnlyadminEdit]
    pagination_class = Pagninationsview
    parser_classes = [MultiPartParser, FormParser]
    queryset = Category.objects.all()


class CategoryDetialsVeiw(RetrieveUpdateDestroyAPIView):
     
    serializer_class = CategorySerializer
    permission_classes = [OnlyadminEdit]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Category.objects.all()
