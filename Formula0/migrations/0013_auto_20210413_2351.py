# Generated by Django 3.0.4 on 2021-04-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formula0', '0012_auto_20210406_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(6, 'ششم'), (7, 'هفتم'), (8, 'هشتم'), (9, 'نهم'), (10, 'دهم'), (11, 'یازدهم'), (12, 'دوازدهم')], null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='team',
            name='voice_chat_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک چت صوتی'),
        ),
    ]
