# Generated by Django 4.0.3 on 2022-04-02 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_alter_useraccountcustommodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountcustommodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c5ef423a-dba2-4349-8aa3-e32050382233'), editable=False, primary_key=True, serialize=False),
        ),
    ]
