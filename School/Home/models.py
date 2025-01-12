from django.db import models

class Notice(models.Model):
    date_uploaded = models.DateTimeField(auto_now_add=True)
    Topic = models.CharField(max_length=100)
    News = models.TextField()
    image = models.ImageField(upload_to='News',blank=True)

    class Mete:
        vartbose_name = 'News'

    def __str__(self):
        return self.Topic
    
    