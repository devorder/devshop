# Generated by Django 4.0.3 on 2022-04-02 20:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0007_alter_useraccountcustommodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountcustommodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e9f23721-53e0-4f45-ba7f-2bff6fb0e80d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
