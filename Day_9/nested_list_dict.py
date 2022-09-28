nested_lD = {
    "city": ["Delhi", "Bangalore", "Fullerton", "Chennai"],
    "movies":{
        "Ram": "Krishna",
        "Allu": "Yavadu",
        "NTR": "RRR"
              }
}

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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })
#to be added to the travel_log. 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)