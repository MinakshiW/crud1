# Generated by Django 5.0.6 on 2024-06-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=34)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=23)),
            ],
        ),
    ]
