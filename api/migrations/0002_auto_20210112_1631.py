# Generated by Django 3.1.5 on 2021-01-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='cId',
        ),
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='teacher',
            field=models.CharField(max_length=20),
        ),
    ]