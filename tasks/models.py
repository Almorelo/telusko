from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    description = models.CharField(max_length=110, default="")
    name = models.CharField(max_length=155, default="")
    # surname = models.CharField(max_length=145, default="")

    def __str__(self):
        return self.title