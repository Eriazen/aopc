from aopc import JSONGetter, JSONParser


x = JSONGetter("https://europe.albion-online-data.com", "/api/v2/stats/prices/", "T4_BAG", "1").get_dict()
print(x)
print(x[0])
print(type(x))