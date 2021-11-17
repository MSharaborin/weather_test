from django.db import models


class Coord(models.Model):
	lon = models.FloatField("Географическое положение города, долгота")
	lat = models.FloatField("Географическое положение города, широта")

	class Meta:
		verbose_name = 'Географическое положение'
		verbose_name_plural = 'Географическое положение'

	def __str__(self):
		return str(self.pk)


class Wind(models.Model):
	speed = models.FloatField(
		"Скорость ветра. Единица "
		"измерения по умолчанию: метр / сек"
	)
	deg = models.IntegerField("Направление ветра, градусы (метеорологические)")
	gust = models.FloatField(
		"Порыв ветра. Единица измерения "
		"по умолчанию: метр / сек",
		default=None, blank=True, null=True
	)

	class Meta:
		verbose_name = 'Параметры ветра'
		verbose_name_plural = 'Параметры ветра'

	def __str__(self):
		return str(self.pk)


class Main(models.Model):
	temp = models.FloatField("Температура. Единица измерения по умолчанию: Цельсий")
	feels_like = models.FloatField(
		"Температура. Этот температурный параметр"
		" объясняет человеческое восприятие погоды."
	)
	temp_min = models.FloatField("Минимальная температура на данный момент.")
	temp_max = models.FloatField("Максимальная температура на данный момент")
	pressure = models.IntegerField("Атмосферное давление")
	humidity = models.IntegerField("Влажность, %")
	sea_level = models.IntegerField(
		"Атмосферное давление на уровне моря, гПа",
		default=None, blank=True, null=True
	)
	grnd_level = models.IntegerField(
		"Атмосферное давление на уровне земли, гПа",
		default=None, blank=True, null=True
	)

	class Meta:
		verbose_name = 'Параметры температуры'
		verbose_name_plural = 'Параметры температуры'

	def __str__(self):
		return str(self.pk)


class Weather(models.Model):
	name = models.CharField('Название города', max_length=255)
	visibility = models.IntegerField("Видимость")
	main = models.ForeignKey('Main', on_delete=models.CASCADE)
	wind = models.ForeignKey('Wind', on_delete=models.CASCADE)
	coord = models.ForeignKey('Coord', on_delete=models.CASCADE)
	dt = models.DateTimeField("Дата", unique=True)

	class Meta:
		verbose_name = 'Погода'
		verbose_name_plural = 'Погода'

	def __str__(self):
		return 'Погода в городе {}, дата: {}'.format(self.name, self.dt)
