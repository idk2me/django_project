from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    published = models.DateField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price
