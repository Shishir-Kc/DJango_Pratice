from django.db import models
from django.contrib.auth.models import User

class Notice(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    Topic = models.CharField(max_length=100)
    News = models.TextField()
    image = models.ImageField(upload_to='News',blank=True)

    class Mete:
        vartbose_name = 'News'

    def __str__(self):
        return self.Topic
    
    