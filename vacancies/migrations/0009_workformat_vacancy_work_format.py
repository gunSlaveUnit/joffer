# Generated by Django 5.0.1 on 2024-02-22 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_delete_skill_alter_vacancy_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='vacancy',
            name='work_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.workformat'),
        ),
    ]
