from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from projman.models import *
from projman.serializers import DepartmentOptionSerializer, EmployeeListSerializer, EmployeeFormSerializer, ProjectOptionSerializer


@swagger_auto_schema(method='GET', responses={200: DepartmentOptionSerializer(many=True)})
@api_view(['GET'])
def department_option_list(request):
    departments = Department.objects.all()
    serializer = DepartmentOptionSerializer(departments, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: ProjectOptionSerializer(many=True)})
@api_view(['GET'])
def project_option_list(request):
    projects = Project.objects.all()
    serializer = ProjectOptionSerializer(projects, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: EmployeeListSerializer(many=True)})
@api_view(['GET'])
def employees_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeListSerializer(employees, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=EmployeeFormSerializer, responses={200: EmployeeFormSerializer()})
@api_view(['POST'])
def employee_form_create(request):
    data = JSONParser().parse(request)
    serializer = EmployeeFormSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=EmployeeFormSerializer, responses={200: EmployeeFormSerializer()})
@api_view(['PUT'])
def employee_form_update(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = EmployeeFormSerializer(employee, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: EmployeeFormSerializer()})
@api_view(['GET'])
def employee_form_get(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee does not exist.'}, status=404)

    serializer = EmployeeFormSerializer(employee)
    return Response(serializer.data)


@api_view(['DELETE'])
def employee_delete(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Employee does not exist.'}, status=404)

    employee.delete()
    return Response(status=204)
