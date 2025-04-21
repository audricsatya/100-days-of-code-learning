travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, number_of_visits, cities_visited):
    travel_log.append({"country": country_visited, "visits": number_of_visits, "cities": cities_visited})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
