from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu/')

    def __str__(self):
        return self.name