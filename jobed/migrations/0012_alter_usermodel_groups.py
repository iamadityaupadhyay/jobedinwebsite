# Generated by Django 5.1.2 on 2024-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('jobed', '0011_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
    ]
