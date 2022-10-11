from django.db import models

# Create your models here.

class Consume(models.Model):
    date = models.DateField()
    cost = models.IntegerField()
    main_category = models.CharField(max_length=15)
    sub_category = models.CharField(max_length=15)
    detail = models.CharField(max_length=20)
    DC = models.BooleanField(default=False)
    fixed_expenses = models.BooleanField(default=False)

    def __str__(self):
        return self.detail