from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class EmployeeContact(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=255)
    emergency_phone = models.CharField(max_length=15)

    def __str__(self):
        self.employee.email

class PerformanceReview(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, unique=True)
    review_date = models.DateField()
    reviewer_name = models.CharField(max_length=255)
    comments = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review for {self.employee.first_name} {self.employee.last_name} on {self.review_date}'

