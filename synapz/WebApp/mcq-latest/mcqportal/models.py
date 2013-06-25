# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Questiondetails(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=900L, db_column='Question', blank=True) # Field name made lowercase.
    optiona = models.CharField(max_length=255L, blank=True)
    optionb = models.CharField(max_length=255L, blank=True)
    optionc = models.CharField(max_length=255L, blank=True)
    optiond = models.CharField(max_length=255L, blank=True)
    answer = models.CharField(max_length=1L, blank=True)
    category = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'QuestionDetails'
    def __unicode__(self):
	return self.question


class Members(models.Model):
    memberid = models.IntegerField(primary_key=True, db_column='Memberid') # Field name made lowercase.
    username = models.CharField(max_length=255L, db_column='Username') # Field name made lowercase.
    email = models.CharField(max_length=255L, db_column='Email') # Field name made lowercase.
    password = models.CharField(max_length=255L, db_column='Password') # Field name made lowercase.
    activation = models.CharField(max_length=40L, db_column='Activation', blank=True) # Field name made lowercase.
    gradyear = models.IntegerField(null=True, db_column='gradYear', blank=True) # Field name made lowercase.
    mobile = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'members'
    def __unicode__(self):
	    return self.username

class answers(models.Model):
    memberid = models.IntegerField(db_column='Memberid') # Field name made lowercase.
    qid = models.ForeignKey('Questiondetails')
    answer = models.CharField(max_length=1L, blank=True)
    def __unicode__(self):
        return self.answer
