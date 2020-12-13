from django.db import models
from datetime import date

class PolicyHolder(models.Model):
    gender = models.CharField(max_length=70, blank=False, default='')
    dob: models.DateField(default=date.date(1900, 1, 1))
    ssn: models.CharField(max_length=9, blank=False, default='')
    smoking: models.BooleanField(default=False)
    allergies = models.CharField(max_length=170, blank=True, default='')
    conditions = models.CharField(max_length=170, blank=True, default='')

class InsuredEvent(models.Model):
    policyHolderId = models.ForeignKey(PolicyHolder, on_delete=models.CASCADE,)
    doi: models.DateField(default=date.today())
    type: models.CharField(max_length=70, blank=False, default='')
    billedAmount: models.DecimalField(max_digits=9, decimal_places=2)
    coveredAmount: models.DecimalField(max_digits=9, decimal_places=2)
