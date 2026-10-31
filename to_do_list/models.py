from django.db import models

# Create your models here.
class task(models.Model):
   
    task=models.TextField(max_length=250,default="write")
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True )
    updated_at=models.DateTimeField(auto_now=True)

    