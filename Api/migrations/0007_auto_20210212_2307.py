# Generated by Django 3.1.6 on 2021-02-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_auto_20210207_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='expire_token',
            field=models.DateTimeField(blank=True, null=True, verbose_name='انقضای توکن'),
        ),
        migrations.AddField(
            model_name='student',
            name='user_token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='توکن'),
        ),
    ]
