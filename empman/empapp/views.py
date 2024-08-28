from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Employee, Department, PerformanceReview
from .serializers import EmployeeSerializer, PerformanceReviewSerializer, EmployeeContactSerializer, DepartmentSerializer
from rest_framework import generics


# Create your views here.
@api_view(['GET'])
def home(request):
    data = {
        'status': 'success',
        'message': 'Welcome to Employee Management API by Agboola Olalekan'
    }
    return Response(data, status=status.HTTP_200_OK)

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PerformanceReviewListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer