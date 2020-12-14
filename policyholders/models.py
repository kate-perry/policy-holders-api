from django.db import models
from datetime import date

class PolicyHolder(models.Model):
    gender = models.CharField(default='', max_length=70, blank=False)
    dob = models.DateField(default=date.today, blank=False)
    ssn = models.CharField(default='', max_length=9, blank=False)
    smoking = models.BooleanField(default=False, null=False)
    allergies = models.CharField(default='', max_length=170, blank=False)
    conditions = models.CharField(default='', max_length=170, blank=False)

class InsuredEvent(models.Model):
    policyHolderId = models.ForeignKey(PolicyHolder, on_delete=models.CASCADE)
    doi = models.DateField(default=date.today, blank=False)
    type = models.CharField(default='', max_length=70, blank=False)
    billedAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=False)
    coveredAmount = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=False)