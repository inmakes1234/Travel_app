# Generated by Django 4.1.7 on 2023-04-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pic')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Travellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=250)),
                ('timg', models.ImageField(upload_to='pic1')),
                ('tdesc', models.TextField()),
            ],
        ),
    ]
