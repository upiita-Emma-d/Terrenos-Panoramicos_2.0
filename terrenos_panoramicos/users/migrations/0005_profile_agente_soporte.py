# Generated by Django 3.2 on 2021-05-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='agente_soporte',
            field=models.BooleanField(default=False, verbose_name='Agente de soporte'),
        ),
    ]
