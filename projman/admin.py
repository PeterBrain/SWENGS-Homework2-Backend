from django.contrib import admin
from projman import models


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Employee, EmployeeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Project, ProjectAdmin)
