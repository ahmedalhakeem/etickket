from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Department(models.Model):
   department_name = models.CharField(max_length=64, null=True, blank=True)

   def __str__(self):
      return f"{self.department_name}"

class Section(models.Model):
   section_name = models.CharField(max_length=64, null=True, blank=True)
   #dept = models.ForeignKey(Department, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.section_name}"
class User(AbstractUser):
   department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept_name", default=None, null=True)
   section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="sect_name", default=None, null=True) 
   pc_code = models.CharField(max_length=10, null=True, blank=True)

class Tickets(models.Model):
   software= 'SW'
   hardware = 'HW'
   
   high_priority = "مهمة جدا"
   normal_priority = "مهمة"
   low_priority = "متوسطة الاهمية"

   select_type = [
      (software, 'software'),
      (hardware, 'hardware')

   ]
   status = [
      (high_priority, 'high_priority'),
      (normal_priority, 'normal_priority'),
      (low_priority, 'low_priority')

   ]

   ticket_type = models.CharField(max_length=2, choices=select_type, default=software,)
   ticket_status= models.CharField(max_length=14, choices=status, default=high_priority,)
   title = models.CharField(max_length=30, blank=True, null=True,)
   description = models.TextField(max_length=100, blank=True, null=True)
   date = models.DateTimeField(auto_now_add=True)
   employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
   it_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="it_user", null=True, blank=True)

   def __str__(self):
      return f"{self.ticket_type}, {self.ticket_status}, {self.title}, {self.description}, on {self.date}, by {self.employee}, solved_by {self.it_user}"
