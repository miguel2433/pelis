# Generated by Django 5.0.4 on 2024-04-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posmovis', '0009_profile_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='edad',
            field=models.DateField(),
        ),
    ]