from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Product(models.Model):
    MAX_NAME = 40

    name = models.CharField(
        max_length=MAX_NAME, null=False, blank=False, )

    product_photo = models.URLField(null=False, blank=False, )

    product_price = models.FloatField(null=False, blank=False, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
