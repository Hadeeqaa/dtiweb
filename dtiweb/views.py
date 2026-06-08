from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import InputUserData,OutputUserData
from .services import outputting_service


class ClothesView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self,request):  
        tier = request.query_params.get('tier')
        count = request.query_params.get('count')


        serializer = InputUserData(data={'tier': tier,'count':count})
        if serializer.is_valid():
            results = outputting_service(
            tier = serializer.validated_data['tier'],
            count = serializer.validated_data['count']
            )
            output = OutputUserData(results,many=True, context = {'request':request})
            return Response(output.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)