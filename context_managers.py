#!/usr/bin/env python3

import json
with open("cities.json") as cities_file:
    cities_data = json.load(cities_file)
    print(cities_data)