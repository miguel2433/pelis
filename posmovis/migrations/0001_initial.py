# Generated by Django 5.0.4 on 2024-04-13 01:10

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]