from django.db import models

class News(models.Model):
    date_uploaded = models.DateTimeField(auto_now_add=True)
    Topic = models.CharField(max_length=100)
    News = models.TextField()
    image = models.ImageField(upload_to='News',blank=True)

    def __str__(self):
        return self.Topic
    
    