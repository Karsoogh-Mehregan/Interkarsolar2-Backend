# Generated by Django 3.0.4 on 2021-04-04 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('national_id', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='نام و نام\u200cخانوادگی')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('name', models.CharField(max_length=40, verbose_name='نام')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='امتیاز')),
                ('student1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_member', to='Formula0.Student', verbose_name='نفر اول')),
                ('student2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_member', to='Formula0.Student', verbose_name='نفر دوم')),
                ('student3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='third_member', to='Formula0.Student', verbose_name='نفر سوم')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
