# Generated by Django 4.2.3 on 2023-09-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sustrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tamanio', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sustrato',
                'verbose_name_plural': 'Sustratos',
                'ordering': ['-tamanio'],
            },
        ),
    ]
