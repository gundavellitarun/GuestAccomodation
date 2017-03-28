from __future__ import unicode_literals

from django.db import models
# from datetime import datetime,timedelta
# from details.views import add_details
# Create your models here.


#Guest Details
class detail(models.Model):
    Gender=models.CharField(max_length=10)
    Indate=models.DateField()
    Outdate=models.DateField()
    name=models.CharField(max_length=25)
    age=models.IntegerField(blank=True)
    relation=models.CharField(max_length=15)
    purpose=models.TextField(blank=True)
    hostelsavailable=models.CharField(max_length=10)


 #  *** NEED USER DATA FROM SSO TO COMPLETE MODEL

# class User(models.Model):
#     """(User description)"""
#
#     access_token = models.CharField(blank=True, max_length=100)
#     refresh_token = models.CharField(blank=True, max_length=100)
#     roll_number = models.CharField(blank=True, max_length=100)
#     first_name = models.CharField(blank=True, max_length=100)
#     last_name = models.CharField(blank=True, max_length=100)
#
#
#     class Admin:
#         list_display = ('',)
#         search_fields = ('',)
#
#     def __unicode__(self):
#         return self.roll_number
#
#
#
# #     #Assuming these rooms are free in respective hostels
# #     indate=detail.Indate
# #     outdate=detail.Outdate
#
#     now=datetime.now()
#     H1=[1,2,3,4,5]
#     H2=[6,7,8,9,10]
#     H3=[11,12,13,14,15]
#     H10=[16,17,18,19,20]
#     H11=[21,22,23,24,25]
#     h1=[]
#     h2=[]
#     h3=[]
#     h10=[]
#     h11=[]
#
#     hostellist=[H1,H2,H3,H10,H11]
#     hostelremoved=[h1,h2,h3,h10,h11]
#
#
#
#
#
#
#
#     #time duration is done
#
#
#
#
#
#
# def roomallocator(a,b):
#     a=hostelsavail.hostellist
#     b=hostelsavail.hostelremoved
#     hostelrequested = detail.hostelsavailable
#
#     for i in range(0, 4):
#         if (hostelrequested == 'a[i]'):
#             b[i].append(a[i].pop(0))
#
#
#
#
#
# def durationdone(a,b,c):
#     a=hostelsavail.hostellist
#     b=hostelsavail.hostelremoved
#     c=detail.Outdate
#     now=datetime.now()
#
#     if((c-now).days==0):
#         a.append(1)
#
#
#
#
# def removehostel(a):
#     a=hostelsavail.hostellist
#
#     for i in range (0,4):
#         if(len(a[i])==0):
#             del a[i]









