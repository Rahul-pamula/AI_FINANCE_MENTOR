from rest_framework import serializers
from .models import UserFinancialData

class UserFinancialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFinancialData
        fields = '__all__'
