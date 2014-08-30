# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Allumini(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'allumini'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Committee(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=30)
    firstname = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=30, blank=True)
    contact_description = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return u'%s : %s %s' % (self.position, self.firstname, self.surname)
    class Meta:
        managed = False
        db_table = 'committee'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Member(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    userpassword = models.CharField(max_length=200, blank=False)
    usertype = models.CharField(db_column='userType', max_length=10, blank=False) # Field name made lowercase.
    def __unicode__(self):
        return u'%s : %s' % (self.username, self.usertype)
    class Meta:
        managed = False
        db_table = 'member'

class News(models.Model):
    newsid = models.BigIntegerField(db_column='newsID', primary_key=True) # Field name made lowercase.
    date = models.DateField(blank=False, null=False)
    title = models.CharField(max_length=30, blank=False)
    contents = models.CharField(max_length=1000, blank=False)
    def __unicode__(self):
        return u'%s : %s' % (self.title, self.date)
    class Meta:
        managed = False
        db_table = 'news'

class Photos(models.Model):
    photos_id = models.BigIntegerField(db_column='imageID', primary_key=True) # Field name made lowercase.
    username = models.ForeignKey(Member, db_column='username', blank=False, null=False)
    name = models.CharField(max_length=50, blank=False)
    url = models.CharField(max_length=50, blank=False)
    datetaken = models.DateField(db_column='dateTaken', blank=False, null=False) # Field name made lowercase.
    type_of_photo = models.CharField(db_column='type',max_length=20, blank=False)
    approved = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return u'%s : %s : %s' % (self.type_of_photo, self.datetaken, self.url)
    class Meta:
        managed = False
        db_table = 'photos'

class Races(models.Model):
    race_id = models.IntegerField(primary_key=True)
    race_name = models.CharField(max_length=50, blank=False)
    def __unicode__(self):
        return u'%s : %s' % (self.race_id, self.race_name)
    class Meta:
        managed = False
        db_table = 'races'

class Results(models.Model):
    result_id = models.IntegerField(primary_key=True)
    year = models.ForeignKey('YearTable')
    race = models.ForeignKey(Races)
    category = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    def __unicode__(self):
        return u'%s : %s : %s : %s' % (self.year.year_value, self.race.race_name, self.category, self.position)
    class Meta:
        managed = False
        db_table = 'results'

class Rower(models.Model):
    username = models.CharField(max_length=20)
    fullname = models.CharField(db_column='fullName', max_length=30, blank=True) # Field name made lowercase.
    photo = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=150, blank=True)
    class Meta:
        managed = False
        db_table = 'rower'

class Videos(models.Model):
    videoid = models.BigIntegerField(db_column='videoID', primary_key=True) # Field name made lowercase.
    name = models.CharField(max_length=50, blank=False)
    url = models.CharField(max_length=50, blank=False)
    dateadded = models.DateField(db_column='dateAdded', blank=False, null=False) # Field name made lowercase.
    def __unicode__(self):
        return u'%s : %s : %s' % (self.name, self.dateadded, self.url)
    class Meta:
        managed = False
        db_table = 'videos'

class YearTable(models.Model):
    year_id = models.IntegerField(primary_key=True)
    year_value = models.CharField(max_length=10, blank=False)
    def __unicode__(self):
        return u'%s : %s' % (self.year_id, self.year_value)
    class Meta:
        managed = False
        db_table = 'year_table'

