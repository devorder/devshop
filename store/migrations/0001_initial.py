# Generated by Django 4.0.3 on 2022-04-02 20:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0006_alter_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10)])),
                ('images', models.ImageField(upload_to='uploads/products')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
