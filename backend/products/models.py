from django.db import models
from general.std_model import StdModel


class Product(StdModel):
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300, null=True, blank=True)
    about = models.CharField(max_length=10000)
    price = models.PositiveSmallIntegerField(default=0)
    customer_price = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey('Category', null=True)
    video = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=30, choices=(
        ('waiting', 'Waiting'), # waiting to pricing or customizing.. should be default
        ('approved', 'Approved'), #ready for selling
        ('closed', 'Closed'), # closed after selling all
    ), db_index=True, default='waiting')
    active = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return u"{0} :::: {1}".format(self.ID, self.name)


class Category(StdModel):
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300, null=True, blank=True)
    about = models.CharField(max_length=10000, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{0} :::: {1}".format(self.ID, self.name)