from django.db import models

# Create your models here.

class Task(models.Model):                                   #The class Task model would create the database 
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)       ##title and complete are fields of the model.
                                                            ##Each field is specified as a class attribute, and each attribute maps to a database column.

    def __str__(self):
        return self.title
