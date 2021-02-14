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
   
   high_priority = "high_priority"
   normal_priority = "normal_priority"
   low_priority = "low_priority"

   accomplished = "accomplished"
   unaccomplished = "unaccomplished"

   status = [
      (accomplished, 'تم الانجاز'),
      (unaccomplished, 'لم يتم الانجاز')
   ]

   select_type = [
      (software, 'software'),
      (hardware, 'hardware')

   ]
   priority = [
      (high_priority, 'high_priority'),
      (normal_priority, 'normal_priority'),
      (low_priority, 'low_priority ')

   ]
   
   ticket_type = models.CharField(max_length=2, choices=select_type, default=software, null=True)
   ticket_priority= models.CharField(max_length=20, choices=priority, default=high_priority, null=True)
   ticket_status = models.CharField(max_length=30, choices=status, default=unaccomplished, null=True)

   title = models.CharField(max_length=30, blank=True, null=True,)
   description = models.TextField(max_length=100, blank=True, null=True)
   date = models.DateTimeField(auto_now_add=True)
   employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
   it_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="it_user", null=True, blank=True)

   def __str__(self):
      return f" {self.id}, {self.ticket_type}, {self.ticket_status}, {self.title}, {self.ticket_priority} {self.description}, by {self.employee}, solved_by {self.it_user}"
