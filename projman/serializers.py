from rest_framework import serializers
from projman import models


class DepartmentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = models.Employee
        fields = ['id', 'first_name', 'last_name', 'dob', 'department']

    def get_department(self, obj):
        return obj.department.name + ' - ' + obj.department.description if obj.department else ''


class EmployeeChartSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = models.Employee
        fields = ['department']

    def get_department(self, obj):
        return obj.department.name + ' - ' + obj.department.description if obj.department else ''


class EmployeeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class ProjectFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'
