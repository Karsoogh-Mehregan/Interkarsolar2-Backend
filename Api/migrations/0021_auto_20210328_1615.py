# Generated by Django 3.0.4 on 2021-03-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0020_auto_20210319_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0, verbose_name='نمره'),
        ),
        migrations.AddField(
            model_name='exam',
            name='min_score',
            field=models.IntegerField(default=0, verbose_name='کمترین نمره'),
        ),
        migrations.CreateModel(
            name='ExamStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('can_register', models.BooleanField(default=False, verbose_name='مجاز به ثبت نام')),
                ('is_preregister', models.BooleanField(default=False, verbose_name='وضعیت پیش ثبت نام')),
                ('is_register_complete', models.BooleanField(default=False, verbose_name='وضعیت ثبت نام نهایی')),
                ('is_pass', models.BooleanField(default=False, verbose_name='قبولی در آزمون')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Api.Exam', verbose_name='آزمون')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Api.Student', verbose_name='دانش آموز')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]