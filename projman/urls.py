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
    path('department/options', views.department_option_list),
    path('project/options', views.project_option_list),
    path('employee/list', views.employees_list),
    path('employee/create', views.employee_form_create),
    path('employee/<int:pk>/get', views.employee_form_get),
    path('employee/<int:pk>/update', views.employee_form_update),
    path('employee/<int:pk>/delete', views.employee_delete),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    url(r'^api-token-auth/', obtain_jwt_token),
]
