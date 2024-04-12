import requests


class WeatherLocation:
    def __init__(self, address):
        self.address: str = address
        self.latitude: str | None = None
        self.longitude: str | None = None
        self.forecast_url: str | None = None
        self.forecast_data: dict | None = None

    def get_coordinates(self):
        url = f"https://nominatim.openstreetmap.org/search?addressdetails=1&q={self.address}&format=jsonv2&limit=1"
        res = requests.get(url=url)
        try:
            self.latitude = res.json()[0]["lat"]
            self.longitude = res.json()[0]["lon"]
        except IndexError:
            print(
                "Could not find latitude & longitude for the given address. Try using a more general location like city and state."
            )

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

