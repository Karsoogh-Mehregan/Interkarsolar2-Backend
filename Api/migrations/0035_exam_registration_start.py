# Generated by Django 3.0.4 on 2021-04-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0034_auto_20210419_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='registration_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='شروع ثبت\u200cنام'),
        ),
    ]