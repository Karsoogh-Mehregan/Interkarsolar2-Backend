# Generated by Django 3.0.4 on 2021-05-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0038_auto_20210515_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='score1',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمره\u200cی تصحیح اول'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='score2',
            field=models.IntegerField(blank=True, null=True, verbose_name='نمره\u200cی تصحیح دوم'),
        ),
    ]
