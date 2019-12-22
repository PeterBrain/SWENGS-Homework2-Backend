from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    path('department/list', views.department_list),
    path('department/options', views.department_list),
    path('department/create', views.department_form_create),
    path('department/<int:pk>/get', views.department_form_get),
    path('department/<int:pk>/update', views.department_form_update),
    path('department/<int:pk>/delete', views.department_delete),
    path('employee/list', views.employees_list),
    path('employee/chart', views.employees_chart),
    path('employee/create', views.employee_form_create),
    path('employee/<int:pk>/get', views.employee_form_get),
    path('employee/<int:pk>/update', views.employee_form_update),
    path('employee/<int:pk>/delete', views.employee_delete),
    path('project/list', views.project_list),
    path('project/options', views.project_list),
    path('project/create', views.project_form_create),
    path('project/<int:pk>/get', views.project_form_get),
    path('project/<int:pk>/update', views.project_form_update),
    path('project/<int:pk>/delete', views.project_delete),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    url(r'^api-token-auth/', obtain_jwt_token),
]
