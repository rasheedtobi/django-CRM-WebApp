from django.db import models


# Create your models here.


class Record(models.Model):
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.state
