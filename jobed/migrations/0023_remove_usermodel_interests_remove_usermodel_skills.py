# Generated by Django 5.1.2 on 2024-11-17 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobed', '0022_interest_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='skills',
        ),
    ]
