# Generated by Django 3.0.4 on 2021-04-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0024_auto_20210329_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(6, 'ششم'), (7, 'هفتم'), (8, 'هشتم'), (9, 'نهم'), (10, 'دهم'), (11, 'یازدهم'), (12, 'دوازدهم')], null=True, verbose_name='پایه تحصیلی'),
        ),
    ]