# Generated by Django 3.2.12 on 2022-12-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
