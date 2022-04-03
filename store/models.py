from django.db import models
import uuid
from django.core.validators import MinValueValidator
from django.urls import reverse
from category.models import Category


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    images = models.ImageField(upload_to="uploads/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"category_slug": self.category.slug, 'product_slug': self.slug})
    