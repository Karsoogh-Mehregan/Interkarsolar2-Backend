# Generated by Django 3.1.6 on 2021-02-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0012_auto_20210219_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان محتوا')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('status', models.IntegerField(default=0, verbose_name='وضعیت')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان آزمون')),
                ('holding_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ برگزاری')),
                ('status', models.IntegerField(default=0, verbose_name='وضعیت')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان سوال')),
                ('status', models.IntegerField(default=0, verbose_name='وضعیت')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_exam', to='Api.exam', verbose_name='آزمون')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('ordering', models.IntegerField(default=0, verbose_name='ترتیب')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='qc_content', to='Api.content', verbose_name='محتوا')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='qc_question', to='Api.question', verbose_name='سوال')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='content',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='content_question', to='Api.question', verbose_name='سوال'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='جواب')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='فایل')),
                ('question_content', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answer_qc', to='Api.questioncontent', verbose_name='محتوای سوال')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answer_student', to='Api.student', verbose_name='دانش آموز')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
