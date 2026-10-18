from math import sqrt
from itertools import combinations

def get_station_data(filename: str) -> dict:
    data = {}
    
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "").split(";")
            if line[0] != "Longitude":
                longitude = float(line[0])
            if line[1] != "Latitude":
                latitude = float(line[1])
            name = line[3]
            
            if name == "name":
                continue
            
            data[name] = (longitude, latitude,) # type: ignore
            
    return data

def distance(stations: dict, station1: str, station2: str) -> float:
    for station in stations:
        if station == station1:
            stat1 = stations[station]
        if station == station2:
            stat2 = stations[station]
            
    longitude1, longitude2 = stat1[0], stat2[0] # type: ignore
    latitude1, latitude2 = stat1[1], stat2[1] # type: ignore
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    
    return sqrt(x_km**2 + y_km**2)

def greatest_distance(stations: dict) -> tuple:
    greatest = 0
    
    for station1, station2 in combinations(stations.keys(), 2):
        dist = distance(stations, station1, station2)
        if dist > greatest:
            greatest = dist
            great_stat1 = station1
            great_stat2 = station2
            
    return great_stat1, great_stat2, greatest # type: ignore


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)