from django.db import models

# Create your models here.

class TodoApp(models.Model):
    title = models.CharField(max_length=255)  # Example max_length of 100 characters
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
    	db_table='TodoApp'


    	
