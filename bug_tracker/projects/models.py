from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
