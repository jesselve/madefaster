from django.db import models

# Create your models here.
class Customer(models.Model):
    openID = models.EmailField()
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    tos_date = models.DateTimeField()
    account_status = models.CharField(max_length=30)
    signup_date = models.DateTimeField()
    referral_source = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer)
    effective_start_date = models.DateTimeField()
    effective_end_date = models.DateTimeField()
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    tos_date = models.DateTimeField()
    account_status = models.CharField(max_length=30)
    signup_date = models.DateTimeField()
    referral_source = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Site(models.Model):
    customer = models.ForeignKey(Customer)
    domain = models.CharField(max_length=50)
    site_status = models.CharField(max_length=30)
    site_tier = models.CharField(max_length=30)
    billing_status = models.CharField(max_length=30)
    last_payment = models.DateTimeField()
    signup_date = models.DateTimeField()
    source_server = models.GenericIPAddressField()
    aws_hosted_zone_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.domain

class SiteHistory(models.Model):
    site = models.ForeignKey(Site)
    effective_start_date = models.DateTimeField()
    effective_end_date = models.DateTimeField()
    customer = models.ForeignKey(Customer)
    domain = models.CharField(max_length=50)
    site_status = models.CharField(max_length=30)
    site_tier = models.CharField(max_length=30)
    billing_status = models.CharField(max_length=30)
    last_payment = models.DateTimeField()
    signup_date = models.DateTimeField()
    source_server = models.GenericIPAddressField()
    aws_hosted_zone_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.domain