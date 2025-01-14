from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField()
    admin_password = models.CharField(max_length=100)
    admin_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.admin_name
    

class UserAccount(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=10)
    user_address = models.TextField()
    user_dob = models.DateField()
    user_profile_pic = models.ImageField(upload_to='UserProfile/ProfilePic/',blank=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'User Account'

class UserProfile(models.Model):
    user_account = models.OneToOneField(UserAccount,on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=99)
    profile_created_at = models.DateTimeField(auto_now_add=True)
    profile_updated_at = models.DateTimeField(auto_now=True)
    user_nick_name = models.CharField(max_length=20,default= 'User')

    def __str__(self):
        time = str(self.profile_updated_at)
        return self.user_nick_name + '`s Profile ' + time

class School_class(models.Model):
    students = models.ManyToManyField(UserAccount)
    class_name = models.CharField(max_length=20)
    class_teacher= models.CharField(max_length=20)
    class_number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'School Class'


    def __str__(self):
        return "class => " + self.class_name+ " | Room Number = > " + str(self.class_number)   