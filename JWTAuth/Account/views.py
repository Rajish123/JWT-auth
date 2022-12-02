from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import UserSerializer,SaleSerializer
from selenium import webdriver
from selenium.webdriver.common.by import By 
from .models import Sale
from .utils import Util

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
class Dashboard(APIView):
    def get(self,request):
        queryset = Sale.objects.all()
        if queryset.exists():
            serializer = SaleSerializer(queryset,many = True)
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })
        else:
            return Response({
                'status':status.HTTP_204_NO_CONTENT,
            })
    
    def post(self,request):
        scrap = Util.scrapper()
        for my_dict in scrap:
            for key,value in my_dict.items():
                sale = Sale(title = key,price = value)
                sale.save()
                continue
        return Response({'data':"successful"})