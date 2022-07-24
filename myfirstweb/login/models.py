from django.db import models

# Create your models here.
class people(models.Model):
    username = models.CharField("用户名",max_length=50, default='')
    password = models.CharField("密码",max_length=50, default='')
    mes = models.CharField("邮件",max_length=50,default='')

class info(models.Model):
    username = models.CharField("用户名", max_length=50, default='')
    password = models.CharField("密码", max_length=50, default='')