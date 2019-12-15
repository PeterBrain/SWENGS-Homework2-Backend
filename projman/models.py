from django.db import models


class Department(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=True,
                                   blank=True)  # blank has to be true, otherwise django admin cannot create a new department

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    dob = models.DateField(null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    projects = models.ManyToManyField('Project', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Project(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    progress = models.PositiveSmallIntegerField(null=True)
    finished = models.BooleanField()

    def __str__(self):
        return self.name
