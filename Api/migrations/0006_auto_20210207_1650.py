# Generated by Django 3.1.6 on 2021-02-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20210206_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='mail',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='پست الکترونیک'),
        ),
    ]