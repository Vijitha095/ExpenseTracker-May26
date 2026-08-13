from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from expense.serailizers import UserSerializer,ExpenseSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class UserView(CreateAPIView):
    serializer_class=UserSerializer

    # def post(self, request, *args, **kwargs):
    #     form_instance=request.data
    #     serializer=UserSerializer(data=form_instance)
    #     if serializer.is_valid():
    #         User.objects.create(**serializer.validated_data)  
    #         User.objects.create_user(**serializer.validated_data)  
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
        
        