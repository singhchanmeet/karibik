from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import EnrollmentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class SubmitForm(APIView):
    
    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({'message': 'Submitted Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            