# Generated by Django 2.2.5 on 2019-09-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_delete_takeorderform'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='active',
            field=models.IntegerField(default=1),
        ),
    ]
