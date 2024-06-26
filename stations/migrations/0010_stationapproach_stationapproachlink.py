# Generated by Django 5.0.3 on 2024-05-01 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0009_rename_answer_examinermarksheet_heading_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationApproach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_points', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_approach', to='stations.thirdlevelstation')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='StationApproachLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('station_approach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_approach_link', to='stations.stationapproach')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
