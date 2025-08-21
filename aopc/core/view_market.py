from ..io.json_getter import JSONGetter


class MarketView:
    def __init__(self,
                 server: str,
                 item: str,
                 quality: str = '1',
                 locations: str | None = None):
        self.ENDPOINT = '/api/v2/stats/prices/'
        self.dict = JSONGetter(server, '/api/v2/stats/prices/', item, quality).get_dict()
        self.data = {}

    def set_data(self):
        for city in self.dict:
            temp = []
            temp.append(city['sell_price_min'])
            temp.append(city['sell_price_max'])
            temp.append(city['buy_price_min'])
            temp.append(city['buy_price_max'])
            self.data[city['city']] = temp

    def get_data(self):
        return self.data