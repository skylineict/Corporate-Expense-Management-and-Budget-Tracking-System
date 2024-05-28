from .models import Income
from rest_framework import serializers


class IncomesSerilizers(serializers.ModelSerializer):
      created_by = serializers.CharField(read_only=True)
      class Meta:
        model = Income
        fields =  [ 'id', 'name', 'amount', 'source', 'description','created_by', 'date' ]

      def validate(self, attrs):
        name = attrs.get('name')
        expens = Income.objects.filter(name=name).exists()
        if expens:
            raise serializers.ValidationError('you have added this income already')
        return super().validate(attrs)
           