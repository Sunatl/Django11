from django.db import models
from django.contrib.auth.models import User

# Модели Group
class Group(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.name


# Модели Students
class Students(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now=True)
    phone = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group, related_name="students") 
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


# Модели Teacher
class Teacher(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=100)  
    group = models.ManyToManyField(Group, related_name="teachers")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name} {self.l_name} - {self.subject}"


# Модели Attendance
class Attendance(models.Model):
    omadan = models.TimeField(auto_now=True, null=True)
    raftan = models.TimeField(auto_now=True, null=True)
    der_mekunam = models.TextField(null=True, blank=True)  
    nameoyam = models.TextField(null=True, blank=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="attendances", null=True)  

    def __str__(self):
        return f"{self.student.f_name} - Attendance"
