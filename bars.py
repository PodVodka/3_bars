import json
import argparse
import math

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def get_biggest_bar(data):
    biggest_bar = max(data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(data):
    smallest_bar = min(data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']

def get_distance(bar, longitude, latitude):
    bar_long = bar['geometry']['coordinates'][0]
    bar_lat = bar['geometry']['coordinates'][1]
    radius = 6371 # km

    dlat = math.radians(bar_lat-latitude)
    dlon = math.radians(bar_long-longitude)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
        * math.cos(math.radians(bar_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data['features'], key=lambda k: get_distance(k, longitude, latitude))
    return closest_bar['properties']['Attributes']['Name']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='path to json file with bars data. '
        'You may download it here: https://devman.org/fshare/1503831681/4/')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    data = load_data(parse_args())
    biggest = get_biggest_bar(data)
    print('Самый вместительный бар:', biggest )
    smallest = get_smallest_bar(data)
    print('Бар с наименьшим количеством посадочных мест:', smallest )
    print('Чтобы найти ближейший бар укажите Ваши координаты')
    longitude = float(input('Введите значение долготы:'))
    latitude = float(input('Введите значение широты:'))
    #longitude, latitude = map(float(input('Введите координаты: долгота, широта')).split())
    closest = get_closest_bar(data,longitude, latitude)
    print('Ближайший к Вам бар:', closest)
