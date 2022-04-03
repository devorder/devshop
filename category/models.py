from distutils.command.upload import upload
import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="public/categories/", blank=True)

    
    class Meta(object):
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("products_by_category", kwargs={"category": self.slug})
        

    def __str__(self) -> str:
        return self.name