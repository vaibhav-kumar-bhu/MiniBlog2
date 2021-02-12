from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=10)
	description=models.TextField()
	Name=models.ForeignKey(User,on_delete=models.CASCADE ,max_length=20 , default='')

class addcomment(models.Model):
	sno=models.AutoField(primary_key=True)
	comment_id=models.IntegerField(null=True)
	comment=models.TextField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(post,on_delete=models.CASCADE)
	parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
	timestamp=models.DateTimeField(default=now)

'''class user(models.Model):
	image=models.ImageField(upload_to='images/%Y/%m/%d')
	name=models.Charfield(max_length=20,default='')
'''