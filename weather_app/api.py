import asyncio
import os
from datetime import datetime

from asgiref.sync import sync_to_async
from ninja import Router
from ninja.errors import HttpError
import httpx

from .scheme import WeatherSchema
from .models import Weather, Main, Wind, Coord


api_weather = Router(tags=['Weather API'])


@api_weather.get('/weather/{city}/{country_code}/', response=WeatherSchema)
async def get_weather(
		request,
		city: str,
		country_code: str,
		dt: datetime = None
):
	"""
	# API для работы с ресурсом.
		https://api.openweathermap.org/data/2.5/weather

		Бесплатная подписка позволяет получать: "Текущие данные о погоде".

	## Обязательные поля:
	****
		city: str (город)
		country_code: str (код страны)
	## Необязательное поле:
	****
		dt: datetime (дата)
		Данное поле для поиска в БД по дате.

	"""
	if dt is not None:
		return await get_weather_from_db(city, dt)
	else:
		data = await task(city, country_code)
		if data[0].get('cod') == '404':
			raise HttpError(404, 'Not Found')
		else:
			await create_weather(*data)
			return dict(*data)


@sync_to_async
def get_weather_from_db(city: str, dt: datetime):
	data = Weather.objects.get(name=city.capitalize(), dt=dt)
	return WeatherSchema.from_orm(data)


@sync_to_async
def create_weather(weather):
	ws = WeatherSchema.parse_obj(weather)
	try:
		main = Main.objects.create(**ws.main.dict())
		coord = Coord.objects.create(**ws.coord.dict())
		wind = Wind.objects.create(**ws.wind.dict())
		return Weather.objects.create(
			name = ws.name,
			visibility = ws.visibility,
			main = main,
			wind = wind,
			coord = coord,
			dt = ws.dt
		)
	except:
		return Weather.objects.get(name=ws.name, dt=ws.dt)


async def request(client, city: str, country_code: str):
	token = os.getenv('TOKEN')
	URL = f"https://api.openweathermap.org/data/2.5/weather?q=" \
	      f"{city},{country_code}&appid={token}&units=metric"
	response = await client.get(URL)
	return response.json()


async def task(city: str, country_code: str):
	async with httpx.AsyncClient() as client:
		tasks = request(client, city, country_code)
		return await asyncio.gather(tasks)
