# Generated by Django 3.0.8 on 2020-08-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countertactic',
            name='formation_image',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='formation_text',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='line_tactics_image',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='line_tactics_text',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='marking_offside_image',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='marking_offside_text',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='style_of_play_image',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='style_of_play_text',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='tackling_index_image',
        ),
        migrations.RemoveField(
            model_name='countertactic',
            name='tackling_index_text',
        ),
        migrations.CreateModel(
            name='CounterTacticWeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=8)),
                ('formation_text', models.CharField(max_length=50)),
                ('formation_image', models.ImageField(upload_to='tactics/formations')),
                ('style_of_play_text', models.CharField(max_length=50)),
                ('style_of_play_image', models.ImageField(upload_to='tactics/style_of_play')),
                ('line_tactics_text', models.CharField(max_length=50)),
                ('line_tactics_image', models.ImageField(upload_to='tactics/line_tactics')),
                ('marking_offside_text', models.CharField(max_length=50)),
                ('marking_offside_image', models.ImageField(upload_to='tactics/marking_offside')),
                ('tackling_index_text', models.CharField(max_length=50)),
                ('tackling_index_image', models.ImageField(upload_to='tactics/tackling_index')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.CounterTactic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CounterTacticStronger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=8)),
                ('formation_text', models.CharField(max_length=50)),
                ('formation_image', models.ImageField(upload_to='tactics/formations')),
                ('style_of_play_text', models.CharField(max_length=50)),
                ('style_of_play_image', models.ImageField(upload_to='tactics/style_of_play')),
                ('line_tactics_text', models.CharField(max_length=50)),
                ('line_tactics_image', models.ImageField(upload_to='tactics/line_tactics')),
                ('marking_offside_text', models.CharField(max_length=50)),
                ('marking_offside_image', models.ImageField(upload_to='tactics/marking_offside')),
                ('tackling_index_text', models.CharField(max_length=50)),
                ('tackling_index_image', models.ImageField(upload_to='tactics/tackling_index')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.CounterTactic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
