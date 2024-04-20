import requests


class Geolocator:
    def __init__(self, address):
        self.address: str = address
        self.latitude: str | None = None
        self.longitude: str | None = None

    def get_coordinates(self):
        url = f"https://nominatim.openstreetmap.org/search?addressdetails=1&q={self.address}&format=jsonv2&limit=1"
        res = requests.get(url=url)
        if res.status_code == 200:
            try:
                self.latitude = res.json()[0]["lat"]
                self.longitude = res.json()[0]["lon"]
            except IndexError:
                print(
                    "Could not find latitude & longitude for the given address. Try using a more general location like city and state."
                )
        else:
            print(f"API request returned a status code of: {res.status_code}")
