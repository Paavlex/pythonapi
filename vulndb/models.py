from django.db import models

# Create your models here.
class Vulnerability(models.Model):
    
    #vytvoreni property typu charfield, nastaveni jeho max delky a defaultni hodnoty
    name = models.CharField(max_length=40, default='-')
    cvss_score = models.CharField(max_length=3, default='-')
    cvss_vector = models.CharField(max_length=110, default='-')
    owasp_score = models.CharField(max_length=7, default='-')
    date = models.CharField(max_length=10, default='-')