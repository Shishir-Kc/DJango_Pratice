from django.db import models


class UserProfile(models.Model):
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
