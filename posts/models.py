from django.db import models

# Create your models here.
class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.title}, {self.body}'