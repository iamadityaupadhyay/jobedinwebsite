# Generated by Django 5.1.2 on 2024-11-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobed', '0024_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_year',
            field=models.CharField(max_length=50),
        ),
    ]
