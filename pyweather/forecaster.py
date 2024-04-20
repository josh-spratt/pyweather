import requests


class Forecaster:
    def __init__(self, latitude, longitude):
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.forecast_url: str | None = None
        self.forecast_data: dict | None = None
    
    def get_forecast_url(self):
        url = f"https://api.weather.gov/points/{self.latitude},{self.longitude}"
        res = requests.get(url=url)
        try:
            self.forecast_url = res.json()["properties"]["forecast"]
        except KeyError:
            print(
                "There was a KeyError trying to parse the forecast url from the response."
            )

    def get_forecast(self):
        if self.forecast_url:
            res = requests.get(url=self.forecast_url)
            self.forecast_data = res.json()
        else:
            print("Cannot get forecast because no forecast_url was set.")
