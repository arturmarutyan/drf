from django.db import models
from django.contrib.auth.models import User

class ProductManager(models.Manager):
    def is_public(self):
        return self.filter(public=True)

    # кастомная логика - проверяем и название и описание на совпадение
    def search(self, query, user=None):
        qs = self.filter(models.Q(title__icontains=query) | models.Q(content__icontains=query))
        qs = qs.is_public()
        if user is not None:
            qs = qs.filter(user=user)
        return qs

class Product(models.Model):
    objects = ProductManager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', default=3)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
