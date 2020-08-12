# Generated by Django 3.0.8 on 2020-08-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0011_auto_20200808_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='image',
        ),
        migrations.AddField(
            model_name='player',
            name='player_image',
            field=models.ImageField(default=1, upload_to='players/player_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='scout_image',
            field=models.ImageField(default=1, upload_to='players/scout_images'),
            preserve_default=False,
        ),
    ]
