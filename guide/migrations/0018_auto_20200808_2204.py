# Generated by Django 3.0.8 on 2020-08-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0017_auto_20200808_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='content',
            field=models.CharField(help_text='Put //...// around a word if you wnat to make it bold', max_length=1000),
        ),
    ]