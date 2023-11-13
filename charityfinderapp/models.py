from django.db import models


# Create your models here.
class Charityinformation(models.Model):
    charity_name = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    district_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=15)
    website = models.URLField(max_length=100)
    open_hours = models.TextField(max_length=400)
    extra_info = models.TextField(max_length=400)

    def __str__(self):
        return self.charity_name

    class Meta:
        db_table = "charityinfo"

