from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from expense.models import Expense

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','email']
        read_only_fields=['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)






class ExpenseSerializer(ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"
        read_only_fields=['id','owner','created_at',]


