# Generated by Django 4.1.1 on 2022-09-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='Black', max_length=255),
        ),
    ]
