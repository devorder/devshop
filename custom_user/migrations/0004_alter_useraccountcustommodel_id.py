# Generated by Django 4.0.3 on 2022-04-02 19:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_alter_useraccountcustommodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountcustommodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7ea0f5a5-93eb-4ed3-ab38-1efeab51a239'), editable=False, primary_key=True, serialize=False),
        ),
    ]