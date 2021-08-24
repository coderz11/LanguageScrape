from django.db import models

# Create your models here.
CATEGORY = (('Local','現地'),('Japan','日本'),('France','フランス'),('Germany','ドイツ'),('Korea', '韓国'),('Spain','スペイン'))

class Schools(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    postdate = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY, default='Local', null=True
    )

    def __str__(self):
        return self.name