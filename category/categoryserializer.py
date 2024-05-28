from rest_framework import serializers
from expense.models import  Category


class CategorySerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField(many=True,read_only=True,)
    income = serializers.StringRelatedField(many=True,read_only=True,)
    image = serializers.ImageField(max_length=1000000,required=False)
 
    class Meta:
        model = Category
      
        fields =  ['name', 'image', 'description','source','pk', 'income']

    def validate(self, attrs):
        name = attrs.get('name')
        category = Category.objects.filter(name=name).exists()
        if category:
            raise serializers.ValidationError('Category already exists, try another name')
        return super().validate(attrs)
           