from django.db import models

class Task(models.Model):
    title = models.CharField('Title', max_length = 250)
    status = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
