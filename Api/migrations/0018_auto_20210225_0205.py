# Generated by Django 3.1.6 on 2021-02-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0017_remove_content_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncontent',
            name='status',
            field=models.IntegerField(default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.IntegerField(choices=[(1, 'متن'), (2, 'ویدئو'), (3, 'عکس'), (4, 'بازی'), (5, 'بازخورد')], default=1, verbose_name='نوع محتوا'),
        ),
    ]
