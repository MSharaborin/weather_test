# Generated by Django 3.2.9 on 2021-11-17 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField(verbose_name='Географическое положение города, долгота')),
                ('lat', models.FloatField(verbose_name='Географическое положение города, широта')),
            ],
            options={
                'verbose_name': 'Географическое положение',
                'verbose_name_plural': 'Географическое положение',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(verbose_name='Температура. Единица измерения по умолчанию: Цельсий')),
                ('feels_like', models.FloatField(verbose_name='Температура. Этот температурный параметр объясняет человеческое восприятие погоды.')),
                ('temp_min', models.FloatField(verbose_name='Минимальная температура на данный момент.')),
                ('temp_max', models.FloatField(verbose_name='Максимальная температура на данный момент')),
                ('pressure', models.IntegerField(verbose_name='Атмосферное давление')),
                ('humidity', models.IntegerField(verbose_name='Влажность, %')),
                ('sea_level', models.IntegerField(blank=True, default=None, null=True, verbose_name='Атмосферное давление на уровне моря, гПа')),
                ('grnd_level', models.IntegerField(blank=True, default=None, null=True, verbose_name='Атмосферное давление на уровне земли, гПа')),
            ],
            options={
                'verbose_name': 'Параметры температуры',
                'verbose_name_plural': 'Параметры температуры',
            },
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField(verbose_name='Скорость ветра. Единица измерения по умолчанию: метр / сек')),
                ('deg', models.IntegerField(verbose_name='Направление ветра, градусы (метеорологические)')),
                ('gust', models.FloatField(blank=True, default=None, null=True, verbose_name='Порыв ветра. Единица измерения по умолчанию: метр / сек')),
            ],
            options={
                'verbose_name': 'Параметры ветра',
                'verbose_name_plural': 'Параметры ветра',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
                ('visibility', models.IntegerField(verbose_name='Видимость')),
                ('dt', models.DateTimeField(unique=True, verbose_name='Дата')),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.coord')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.main')),
                ('wind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_app.wind')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода',
            },
        ),
    ]
