from rest_framework import serializers
from projman import models


class DepartmentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name', 'description']


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = models.Employee
        fields = ['id', 'first_name', 'last_name', 'dob', 'department']

    def get_department(self, obj):
        return obj.department.name if obj.department else ''


class EmployeeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'first_name', 'last_name', 'dob', 'department'] #'__all__'


class ProjectFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'progress', 'finished']
