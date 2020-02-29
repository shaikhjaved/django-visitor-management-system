from django.db import models

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=191, default=None)
    company_phone = models.CharField(max_length=15, default=None)
    company_owner = models.CharField(max_length=191, default=None)
    company_address = models.CharField(max_length=191, default=None)
    contact_person = models.CharField(max_length=191, default=None)
    company_email = models.EmailField(default=None)

    def __str__(self):
        return self.company_name
