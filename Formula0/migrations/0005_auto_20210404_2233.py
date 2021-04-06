# Generated by Django 3.0.4 on 2021-04-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formula0', '0004_auto_20210404_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='subject',
            field=models.IntegerField(choices=[(0, 'اقتصاد - سطح ۱'), (1, 'اقتصاد - سطح ۲'), (2, 'ریاضی - سطح ۱'), (3, 'ریاضی - سطح ۲'), (4, 'زیست - سطح ۱'), (5, 'زیست - سطح ۲'), (6, 'شیمی - سطح ۱'), (7, 'شیمی - سطح ۲'), (8, 'فیزیک - سطح ۱'), (9, 'فیزیک - سطح ۲'), (10, 'کامپیوتر - سطح ۱'), (11, 'کامپیوتر - سطح ۲'), (12, 'نجوم - سطح ۱'), (13, 'نجوم - سطح ۲')], max_length=40, null=True, verbose_name='موضوع'),
        ),
    ]