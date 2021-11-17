import asyncio
from datetime import datetime

from asgiref.sync import sync_to_async
from ninja import Router
import httpx

from .scheme import WeatherSchema
from .models import Weather, Main, Wind, Coord


api_weather = Router(tags=['Weather API'])


@api_weather.get('/weather/{city}/{country_code}/', response=WeatherSchema)
async def get_weather(request, city: str, country_code: str, dt: datetime = None):
	"""
		/{city}/{country_code}/
		city: str, country_code: str
	:return:
	"""

	try:
		data = await get_weather_from_db(city, dt)
		return data
	except:
		data = await task(city, country_code)
		await create_weather(*data)
		return dict(*data)


@sync_to_async
def get_weather_from_db(city, dt):
	result = Weather.objects.get(name=city, dt=dt)
	return WeatherSchema.from_orm(result)


@sync_to_async
def create_weather(weather):
	ws = WeatherSchema.parse_obj(weather)
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


async def request(client, city, country_code):
	token = '0d487576bb305f408d49d6bf7872d7f9'
	URL = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={token}&units=metric"
	response = await client.get(URL)
	print(response.status_code)
	return response.json()


async def task(city, country_code):
	async with httpx.AsyncClient() as client:
		tasks = request(client, city, country_code)
		return await asyncio.gather(tasks)
