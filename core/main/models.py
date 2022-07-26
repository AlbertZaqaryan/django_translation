from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Car name', max_length=50, null=True)
    text = models.TextField('Car text')

    def __str__(self):
        return self.title


