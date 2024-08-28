from rest_framework import serializers
from .models import Department, Employee, PerformanceReview, EmployeeContact


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_name = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )
    #department_name = DepartmentSerializer(write_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContact
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_name = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )
    class Meta:
        model = PerformanceReview
        fields = '__all__'
    