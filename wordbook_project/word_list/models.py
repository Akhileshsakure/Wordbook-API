from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=100)
    meaning = ArrayField(
        models.CharField(max_length=512)
    )
    usage = ArrayField(
        models.CharField(max_length=512)
    )

    def __str__(self):
        return self.word