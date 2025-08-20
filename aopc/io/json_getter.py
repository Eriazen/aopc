from urllib.request import urlopen
from urllib.parse import quote
from json import loads


class JSONGetter:
    def __init__(self,
                 server: str,
                 endpoint: str,
                 items: str,
                 qualities: str,
                 locations: str | None = None) -> None:
        self.CITIES = "5003,Black Market,Bridgewatch,Carleon,Fort Sterling,Lymhurst,Martlock,Thetford"

        if not locations:
            locations = self.CITIES

        self.request = f"{server}/{quote(endpoint)}/{quote(items)}.json?locations={quote(locations)}&qualities={quote(qualities)}"
        self.url_response = None

        self.reload_url()

    def get_dict(self) -> str:
        return loads(self.url_response.read())

    def reload_url(self) -> None:
        self.url_response = urlopen(self.request)