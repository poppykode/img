# Generated by Django 5.0.3 on 2024-04-28 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0008_alter_candidateinstruction_heading_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examinermarksheet',
            old_name='answer',
            new_name='heading',
        ),
        migrations.CreateModel(
            name='ExaminerMarkSheetAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('examiner_mark_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examiner_mark_sheet_answer', to='stations.examinermarksheet')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]