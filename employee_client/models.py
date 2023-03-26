import datetime
import time

from django.db import models
from django.utils import timezone


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def get_age(self):
        return int((datetime.date.today() - self.birth_date).days / 365)

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.PositiveIntegerField()
    work_experience = models.DateField()


class Passport(models.Model):
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=9)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="passport")

    def get_gender(self):
        if self.inn.startswith("2"):
            return "Male"
        return "Female"


class WorkProject(models.Model):
    project_name = models.CharField(max_length=30)
    employees = models.ManyToManyField(Employee, related_name="work_projects", through="Membership")


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)


class Client(AbstractPerson):
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)


class VIPClient(Client):
    vip_status_start = models.DateTimeField(auto_now=True)
    donation_amount = models.IntegerField()
