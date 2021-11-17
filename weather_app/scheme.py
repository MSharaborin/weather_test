from ninja.orm import create_schema

from .models import Weather


WeatherSchema = create_schema(
	Weather,
	depth=1,
	fields=['name', 'visibility', 'main', 'wind', 'coord', 'dt']
)
