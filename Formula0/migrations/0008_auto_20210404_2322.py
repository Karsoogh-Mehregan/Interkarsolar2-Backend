# Generated by Django 3.0.4 on 2021-04-04 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formula0', '0007_auto_20210404_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemteam',
            name='answer',
            field=models.TextField(null=True, verbose_name='پاسخ'),
        ),
        migrations.AddField(
            model_name='team',
            name='voice_chat_link',
            field=models.CharField(max_length=255, null=True, verbose_name='لینک چت صوتی'),
        ),
    ]
