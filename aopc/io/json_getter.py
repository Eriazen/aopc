from urllib.request import urlopen
from urllib.parse import quote
from json import loads


class JSONGetter:
    def __init__(self,
                 server: str,
                 endpoint: str,
                 items: str,
                 locations: str | None = None,
                 qualities: str | None = None) -> None:
        self.CITIES = "5003,Black Market,Bridgewatch,Carleon,Fort Sterling,Lymhurst,Martlock,Thetford"
        self.QUALITIES = "1,2,3,4,5"

        if not locations:
            locations = self.CITIES
        if not qualities:
            qualities = self.QUALITIES
        self.request = f"{server}/{quote(endpoint)}/{quote(items)}.json?locations={quote(locations)}&qualities={quote(qualities)}"
        print(self.request)
        self.url_response = None

        self.reload_url()

    def get_json(self) -> str:
        return loads(self.url_response.read())

    def reload_url(self) -> None:
        self.url_response = urlopen(self.request)