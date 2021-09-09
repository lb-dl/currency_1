from django.test import TestCase
from unittest import mock
from weather.utils.logic import WeatherHandler
from weather.test_data.weather_data import CITY, WEATHER_DATA
from hotels.models import City
from weather.models import Weather


class TestWeatherModel(TestCase):

    @mock.patch('weather.utils.logic.get_weather_from_api', return_value=WEATHER_DATA)
    def test_get_weather_from_api_and_create_model(self, mock):

        instance = WeatherHandler(CITY['city_name'])
        city_name = instance.get_city_from_city_model()
        instance.get_weather_from_api_and_create_model()
        weather_in_city = Weather.objects.filter(city=city_name).first()

        self.assertEqual(len(Weather.objects.filter(city=city_name).all()), 4)
        self.assertEqual(weather_in_city.current_temp, 20.66)

        weather_in_city = Weather.objects.filter(city=city_name).last()

        self.assertEqual(weather_in_city.description, 'clear sky')

    @mock.patch('weather.utils.logic.get_weather_from_api')
    def test_create_weather_in_city(self, mock):
        instance = WeatherHandler(CITY['city_name'])
        city_name = instance.get_city_from_city_model()
        data = WEATHER_DATA['forecast'][0]
        instance.create_weather_in_city(data['current_temp'], data['feels_like'], data['description'],
                               data['humidity'], data['wind'], data['clouds'], data['max_temp'],
                                data['min_temp'], data['current_date'], data['icon'])
        weather_in_city = Weather.objects.filter(city=city_name).first()

        self.assertEqual(len(Weather.objects.filter(city=city_name).all()), 1)
        self.assertEqual(weather_in_city.current_temp, 20.66)
        self.assertEqual(weather_in_city.description, 'clear sky')

    def test_get_city_from_city_model(self, city=CITY['city_name']):
        instance = WeatherHandler(city)
        instance.get_city_from_city_model()

        self.assertTrue(City.objects.get(name=city))
        self.assertEqual(len(City.objects.filter(name=city).all()), 1)

    def tearDown(self):
        City.objects.all().delete()
        Weather.objects.all().delete()
