from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )
    image = models.ImageField(upload_to='posts/%y/%m/%d', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    publisher = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
