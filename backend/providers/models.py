from django.db import models
from general.std_model import StdModel


class Provider(StdModel):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=10000, null=True, blank=True)
    active = models.BooleanField(default=False)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    site = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{0} :::: {1}".format(self.ID, self.name)