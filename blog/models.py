from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)


class PostTag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("post", "tag")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00"))
    image = models.ImageField(
        upload_to="media/%y/%m/%d", null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tag = models.ManyToManyField(
        Tag, through=PostTag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    publisher = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
