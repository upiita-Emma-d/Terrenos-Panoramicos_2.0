# Generated by Django 3.1.4 on 2021-01-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='curp',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='profile',
            name='ine',
            field=models.ImageField(blank=True, null=True, upload_to='users/ine'),
        ),
    ]
