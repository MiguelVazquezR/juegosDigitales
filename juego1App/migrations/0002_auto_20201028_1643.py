# Generated by Django 2.2.3 on 2020-10-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego1App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='codigo',
            field=models.CharField(max_length=35),
        ),
    ]
