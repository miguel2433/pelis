# Generated by Django 5.0.4 on 2024-04-20 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_agregar_cap_generos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agregar_cap',
            name='generos',
        ),
        migrations.AddField(
            model_name='series',
            name='generos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.genero'),
        ),
    ]