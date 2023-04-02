import unittest
import requests


class TestWeatherData(unittest.TestCase):

    def test_connection(self):
        url = "http://localhost:8082/get_data?data_type=weather&snippet=false"

        response = requests.get(url)
        print(response.status_code)

        self.assertEqual(response.status_code, 200)


    def test_get_meta(self):
        url = "http://localhost:8082/get_meta"

        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("weather", data)

        column_names = data["weather"].split(", ")
        print("Table Name: weather")
        print("Column Names:")
        for column in column_names:
            print(column)

    def test_check_weather_integrity(self):
        url = "http://localhost:8082/get_data?data_type=weather&snippet=false"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        weathers = data["@list"][:]
        for weather in weathers:
            self.assertIsNotNone(weather["dataTime"])
            self.assertIsNotNone(weather["irradiance"])
            self.assertIsNotNone(weather["precipitation"])
            self.assertIsNotNone(weather["temperature"])
            self.assertIsNotNone(weather["humidity"])
            self.assertIsNotNone(weather["windSpeedAVG"])
            self.assertIsNotNone(weather["illuminance"])
            self.assertIsNotNone(weather["windSpeedGust"])
        print("test_check_weather_integrity: PASSED")


    def test_get_weather_data_false(self):
        url = "http://localhost:8082/get_data?data_type=weather&snippet=false"

        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        weathers = data["@list"][:]
        for weather in weathers:
            print(f"id: {weather['id']}, datatime: {weather['dataTime']}, irradiance: {weather['irradiance']}, precipitation: {weather['precipitation']}, temperature: {weather['temperature']}, humidity: {weather['humidity']}, windSpeedAVG: {weather['windSpeedAVG']}, illuminance: {weather['illuminance']}, windSpeedGust: {weather['windSpeedGust']}")

    def test_get_weather_data_false_true(self):
        url = "http://localhost:8082/get_data?data_type=weather&snippet=false"

        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        weathers = data["@list"][:20]
        for weather in weathers:
            print(f"id: {weather['id']}, datatime: {weather['dataTime']}, irradiance: {weather['irradiance']}, precipitation: {weather['precipitation']}, temperature: {weather['temperature']}, humidity: {weather['humidity']}, windSpeedAVG: {weather['windSpeedAVG']}, illuminance: {weather['illuminance']}, windSpeedGust: {weather['windSpeedGust']}")


if __name__ == '__main__':
    unittest.main()
