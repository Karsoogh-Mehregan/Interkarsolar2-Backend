# Generated by Django 3.0.4 on 2021-04-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formula0', '0006_auto_20210404_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='grade',
            field=models.IntegerField(choices=[(6, 'ششم'), (7, 'هفتم'), (8, 'هشتم'), (9, 'نهم'), (10, 'دهم'), (11, 'یازدهم'), (12, 'دوازدهم')], null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='شناسه'),
        ),
    ]
