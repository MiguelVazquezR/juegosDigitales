# Generated by Django 2.2.3 on 2020-10-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('juego', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'participante',
                'verbose_name_plural': 'participantes',
            },
        ),
    ]
