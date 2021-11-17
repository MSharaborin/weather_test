from ninja import NinjaAPI
from weather_app.api import api_weather


api = NinjaAPI(title='Weather Api', version='0.0.1',)

api.add_router('', api_weather)