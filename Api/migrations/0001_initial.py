# Generated by Django 3.1.6 on 2021-02-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایشی')),
                ('order_id', models.CharField(max_length=50, verbose_name='آی دی پرداخت')),
                ('amount', models.IntegerField(verbose_name='مبلغ')),
                ('name', models.CharField(max_length=255, verbose_name='نام پرداخت کننده')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('mail', models.CharField(max_length=255, verbose_name='پست الکترونیک')),
                ('desc', models.CharField(max_length=255, verbose_name='توضیح تراکنش')),
                ('callback', models.CharField(max_length=2048, verbose_name='آدرس بازگشت')),
                ('pay_id', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='آی دی پرداخت')),
                ('pay_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='لینک پرداخت')),
                ('status', models.IntegerField(blank=True, null=True, verbose_name='وضعیت تراکنش')),
                ('track_id', models.IntegerField(blank=True, null=True, verbose_name='کد رهگیری آیدی پی')),
                ('card_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره کارت پرداخت کننده با فرمت')),
                ('hashed_card_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='هش شماره کارت پرداخت کننده')),
                ('date', models.IntegerField(blank=True, null=True, verbose_name='زمان پرداخت تراکنش')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]