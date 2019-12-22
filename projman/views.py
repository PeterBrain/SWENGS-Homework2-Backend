from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from projman.models import *
from projman.serializers import DepartmentFormSerializer, EmployeeListSerializer, EmployeeFormSerializer, \
    ProjectFormSerializer, EmployeeChartSerializer


@swagger_auto_schema(method='GET', responses={200: DepartmentFormSerializer(many=True)})
@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentFormSerializer(departments, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=DepartmentFormSerializer, responses={200: DepartmentFormSerializer()})
@api_view(['POST'])
def department_form_create(request):
    data = JSONParser().parse(request)
    serializer = DepartmentFormSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=DepartmentFormSerializer, responses={200: DepartmentFormSerializer()})
@api_view(['PUT'])
def department_form_update(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Department does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = DepartmentFormSerializer(department, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: DepartmentFormSerializer()})
@api_view(['GET'])
def department_form_get(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Department does not exist.'}, status=404)

    serializer = DepartmentFormSerializer(department)
    return Response(serializer.data)


@api_view(['DELETE'])
def department_delete(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'error': 'Department does not exist.'}, status=404)

    department.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: EmployeeListSerializer(many=True)})
@api_view(['GET'])
def employees_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeListSerializer(employees, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: EmployeeChartSerializer(many=True)})
@api_view(['GET'])
def employees_chart(request):
    employees = Employee.objects.all()
    serializer = EmployeeChartSerializer(employees, many=True)
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
    except Employee.DoesNotExist:
        return Response({'error': 'Employee does not exist.'}, status=404)

    employee.delete()
    return Response(status=204)


@swagger_auto_schema(method='GET', responses={200: ProjectFormSerializer(many=True)})
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectFormSerializer(projects, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=ProjectFormSerializer, responses={200: ProjectFormSerializer()})
@api_view(['POST'])
def project_form_create(request):
    data = JSONParser().parse(request)
    serializer = ProjectFormSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=ProjectFormSerializer, responses={200: ProjectFormSerializer()})
@api_view(['PUT'])
def project_form_update(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = ProjectFormSerializer(project, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: ProjectFormSerializer()})
@api_view(['GET'])
def project_form_get(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project does not exist.'}, status=404)

    serializer = ProjectFormSerializer(project)
    return Response(serializer.data)


@api_view(['DELETE'])
def project_delete(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project does not exist.'}, status=404)

    project.delete()
    return Response(status=204)
