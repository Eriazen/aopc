from aopc import JSONGetter
from aopc import MarketView


# x = JSONGetter("https://europe.albion-online-data.com", "/api/v2/stats/prices/", "T4_BAG", "1").get_dict()
# print(x)
# print(x[0])
# print(type(x))

view = MarketView('https://europe.albion-online-data.com', 'T4_BAG')
view.set_data()
print(view.get_data())