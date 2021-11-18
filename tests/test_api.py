import pytest

from weather_app.api import task, create_weather, get_weather_from_db
from .json_test import scheme


class TestApi:

	@pytest.mark.asyncio
	@pytest.mark.parametrize('city, code, status_code', [
		('Moscow', 'ru', 200),
		('Yakutsk', 'ru', 200),
		('Ошибка', 'ошибка', '404')
	])
	async def test_task_response_apiopenweathermap(self, city, code, status_code):
		response = await task(city, code)
		assert response[0].get('cod') == status_code

	@pytest.mark.asyncio
	@pytest.mark.django_db
	async def test_create_weather(self):
		response = await create_weather(weather=scheme)
		assert response.pk == 1

	@pytest.mark.asyncio
	@pytest.mark.django_db
	@pytest.mark.parametrize('city, dt, result', [
		('Yakutsk', '2021-11-18 02:26:54+00:00', 'Yakutsk')])
	async def test_get_weather_from_db(self, city, dt, result):
		response = await get_weather_from_db(city, dt)
		assert response.name == result

	@pytest.mark.django_db
	@pytest.mark.parametrize('city, country_code, result', [
		('Vladivostok', 'ru', 200),
		('London', 'uk', 200),
		('Ошибка', 'ошибка', 404)
	])
	def test_get_weather_api(self, client, city, country_code, result):
		url = f'/api/v1/weather/{city}/{country_code}/'

		response = client.get(url)
		assert response.status_code == result
