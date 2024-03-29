# Generated by Django 3.1.6 on 2021-02-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_payment_return_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='manager_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='نام مدیر مدرسه'),
        ),
        migrations.AddField(
            model_name='student',
            name='manager_phone',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='شماره مدیر مدرسه'),
        ),
        migrations.AddField(
            model_name='student',
            name='school_phone',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='شماره تلفن مدرسه'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(7, 'هفتم'), (8, 'هشتم'), (9, 'نهم'), (10, 'دهم')], null=True, verbose_name='پایه تحصیلی'),
        ),
    ]
