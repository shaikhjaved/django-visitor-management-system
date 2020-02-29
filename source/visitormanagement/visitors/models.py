from django.db import models
from companies.models import Company
# Create your models here.


class Visitor(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=191)
    visitor_phone = models.CharField(max_length=15)
    visitor_from = models.CharField(max_length=191)
    purpose_of_visit = models.CharField(max_length=191)
    visit_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    check_in = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    check_out = models.DateTimeField('check_out', blank=True, null=True)
    barcode = models.CharField(max_length=225, blank=True, null=True)
    visitor_image = models.TextField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return self.visitor_name
