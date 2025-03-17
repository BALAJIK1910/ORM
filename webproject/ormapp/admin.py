from django.contrib import admin
from .models import Employee
from .models import EmployeeAdmin

admin.site.register(Employee, EmployeeAdmin)
