# Generated by Django 3.1.7 on 2021-10-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
