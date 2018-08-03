import json
import argparse
import math


def load_data(filepath):

    with open(filepath, 'r') as f:
        bars_list = json.load(f)
    return bars_list


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']


def get_distance(bar, longitude, latitude):
    bar_long = bar['geometry']['coordinates'][0]
    bar_lat = bar['geometry']['coordinates'][1]
    radius = 6371

    dlat = math.radians(bar_lat-latitude)
    dlon = math.radians(bar_long-longitude)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
        * math.cos(math.radians(bar_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance


def get_closest_bar(bars_list, longitude, latitude):
    closest_bar = min(bars_list['features'], key=lambda k: get_distance(k, longitude, latitude))
    return closest_bar['properties']['Attributes']['Name']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='You may download it here: https://devman.org/fshare/1503831681/4/')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    bars_list = load_data(parse_args())
    biggest = get_biggest_bar(bars_list)
    print('Самый вместительный бар:', biggest)
    smallest = get_smallest_bar(bars_list)
    print('Бар с наименьшим количеством посадочных мест:', smallest)
    print('Чтобы найти ближейший бар укажите Ваши координаты')
    longitude = float(input('Введите значение долготы:'))
    latitude = float(input('Введите значение широты:'))
    closest = get_closest_bar(bars_list, longitude, latitude)

    print('Ближайший к Вам бар:', closest)
