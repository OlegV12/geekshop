# Generated by Django 3.1 on 2020-08-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20200820_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
