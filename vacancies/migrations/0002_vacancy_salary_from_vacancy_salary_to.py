# Generated by Django 5.0.1 on 2024-01-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
