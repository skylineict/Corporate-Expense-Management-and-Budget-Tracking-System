from rest_framework import serializers
from .models import Expenses
from .models import Category



class ExpensiveSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Expenses
        fields =  ['name', 'amount', 'category', 'description']

    def validate(self, attrs):
        name = attrs.get('name')
        expens = Expenses.objects.filter(name=name).exists()
        if expens:
            raise serializers.ValidationError('you have added this expenses already')
        return super().validate(attrs)
           


