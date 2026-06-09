from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import InputUserData,OutputUserData,UserRegistrationData
from .services import outputting_service
from .models import Userdti


class UserView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self,request):
        serializer = UserRegistrationData(data=request.data) 
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            Userdti.objects.create_user(username=username, password=password)
            return Response({'message':'user created <3'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class ClothesView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):  
        tier = request.user.tier
        count = request.query_params.get('count')


        serializer = InputUserData(data={'tier': tier,'count':count})
        if serializer.is_valid():
            results = outputting_service(
                tier=tier,
            count = serializer.validated_data['count']
            )
            output = OutputUserData(results,many=True, context = {'request':request})
            return Response(output.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
