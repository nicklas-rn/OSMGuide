# Generated by Django 3.0.8 on 2020-08-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0021_auto_20200810_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beginnertip',
            name='content',
            field=models.CharField(help_text='BOLD: //x// to make x bold                    LINK: --x@/link@-- to go page link with text x', max_length=1000),
        ),
        migrations.AlterField(
            model_name='player',
            name='content',
            field=models.CharField(help_text='BOLD: //x// to make x bold                    LINK: --x@/link@-- to go page link with text x', max_length=1000),
        ),
        migrations.AlterField(
            model_name='tip',
            name='content',
            field=models.CharField(help_text='BOLD: //x// to make x bold                    LINK: --x@/link@-- to go page link with text x', max_length=1000),
        ),
    ]
