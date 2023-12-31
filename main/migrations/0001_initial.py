# Generated by Django 4.2.5 on 2023-09-11 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('effect', models.TextField(default='')),
                ('value', models.IntegerField(default=0)),
            ],
        ),
    ]
