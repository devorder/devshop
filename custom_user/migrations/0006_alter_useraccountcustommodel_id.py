# Generated by Django 4.0.3 on 2022-04-02 19:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0005_alter_useraccountcustommodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountcustommodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('91dca590-fa4e-4dad-9285-7700c92c012a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
