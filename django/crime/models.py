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

class Alert(models.Model):
    alertid = models.IntegerField(primary_key=True, db_column='alertID') # Field name made lowercase.
    jailid = models.IntegerField(null=True, db_column='jailID', blank=True) # Field name made lowercase.
    sent = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'alert'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Inmate(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    lastname = models.CharField(max_length=20L, db_column='LastName', blank=True) # Field name made lowercase.
    firstname = models.CharField(max_length=20L, db_column='FirstName', blank=True) # Field name made lowercase.
    height = models.CharField(max_length=15L, blank=True)
    weight = models.CharField(max_length=3L, blank=True)
    sex = models.CharField(max_length=1L, blank=True)
    eye = models.CharField(max_length=5L, blank=True)
    hair = models.CharField(max_length=5L, blank=True)
    race = models.CharField(max_length=1L, blank=True)
    pod = models.CharField(max_length=4L, blank=True)
    offense = models.CharField(max_length=9000L, blank=True)
    active = models.CharField(max_length=1L, blank=True)
    in_time = models.DateTimeField(auto_now = False, auto_now_add = True, null=False, blank = False)
    last_seen = models.DateTimeField(auto_now = False, auto_now_add = True, null=False, blank = False)
    mugshot = models.CharField(max_length=50L, blank=True)
    gcid = models.CharField(max_length=20L, blank=True)
    jailid = models.CharField(max_length=20L, db_column='jailID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'inmate'

class Inmatewatchlist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=75L)
    reason = models.CharField(max_length=75L, db_column='REASON', blank=True) # Field name made lowercase.
    active = models.CharField(max_length=1L)
    departmentid = models.IntegerField(db_column='departmentID') # Field name made lowercase.
    class Meta:
        db_table = 'inmatewatchlist'

class Offense(models.Model):
    offenseid = models.IntegerField(primary_key=True, db_column='offenseID') # Field name made lowercase.
    greenecoid = models.CharField(max_length=10L, blank=True)
    jailid = models.CharField(max_length=10L, blank=True)
    warrantno = models.CharField(max_length=25L, db_column='warrantNo', blank=True) # Field name made lowercase.
    offense = models.CharField(max_length=100L, blank=True)
    bond = models.CharField(max_length=10L, blank=True)
    offenselevel = models.CharField(max_length=5L, db_column='offenseLevel', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'offenses'

class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey('PollsPoll')
    choice_text = models.CharField(max_length=200L)
    votes = models.IntegerField()
    class Meta:
        db_table = 'polls_choice'

class PollsPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=200L)
    pub_date = models.DateTimeField()
    class Meta:
        db_table = 'polls_poll'

class Testinmatelist(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=20L)
    first_name = models.CharField(max_length=20L)
    time_in = models.DateTimeField()
    timeout = models.CharField(max_length=40L, blank=True)
    active = models.CharField(max_length=1L, blank=True)
    gcid = models.CharField(max_length=15L, blank=True)
    class Meta:
        db_table = 'testinmatelist'

class WatchList(models.Model):
    name = models.CharField(max_length=50L, blank=True)
    sent = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'watch_list'

class Watchlist(models.Model):
    name = models.CharField(max_length=50L, blank=True)
    sent = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'watchlist'

class Department(models.Model):
    deptid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'department'

class People(models.Model):
    peopleid = models.IntegerField(primary_key=True, db_column='peopleID') # Field name made lowercase.
    firstname = models.CharField(max_length=20L, blank=True)
    lastname = models.CharField(max_length=20L, blank=True)
    department = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15L, blank=True)
    email = models.CharField(max_length=50L, blank=True)
    jailid = models.CharField(max_length=20L, db_column='jailID', blank=True) # Field name made lowercase.
    agency = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'people'

class Project(models.Model):
    projectid = models.IntegerField(primary_key=True, db_column='projectID') # Field name made lowercase.
    departmentid = models.IntegerField(null=True, db_column='departmentID', blank=True) # Field name made lowercase.
    peopleid = models.IntegerField(null=True, db_column='peopleID', blank=True) # Field name made lowercase.
    projectdata = models.CharField(max_length=30L, db_column='projectData', blank=True) # Field name made lowercase.
    projectdescription = models.CharField(max_length=1000L, blank=True)
    class Meta:
        db_table = 'project'

class Sunshinerequest(models.Model):
    requestid = models.IntegerField(primary_key=True, db_column='requestID') # Field name made lowercase.
    requestagency = models.CharField(max_length=50L, blank=True)
    requestdate = models.DateTimeField(null=True, blank=True)
    responsedate = models.DateTimeField(null=True, blank=True)
    response = models.CharField(max_length=1000L, blank=True)
    personid = models.IntegerField(null=True, db_column='personID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'sunshinerequest'

