from django.db import models

# Create your models here.
class list(models.Model):
    Add_list = models.CharField(max_length=100)
    Status = models.BooleanField(default=False)

def _str_(self):
    return "{}".format(self.name)