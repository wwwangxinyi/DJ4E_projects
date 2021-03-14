from django.db import models
from django.core.validators import MinLengthValidator

class Brand(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Brand must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Gadget(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    price = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    notes = models.CharField(max_length=300)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname