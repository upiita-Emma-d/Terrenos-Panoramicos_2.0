# Generated by Django 3.2 on 2021-04-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_auto_20210107_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
