import json
import argparse
from math import sqrt


def load_from_json(filepath):

    with open(filepath, 'r') as file_object:
        try:
            return json.load(file_object)
        except json.decoder.JSONDecodeError:
            return None


def get_biggest_bar(bars_list):
    return max(bars_list, key=get_seats_count)


def get_smallest_bar(bars_list):
    return min(bars_list, key=get_seats_count)


def get_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_distance(bar, longitude, latitude):
    bar_long = bar['geometry']['coordinates'][0]
    bar_lat = bar['geometry']['coordinates'][1]
    return sqrt((bar_long - longitude) ** 2 + (bar_lat - latitude) ** 2)


def get_closest_bar(bars_list, longitude, latitude):
    return min(bars_list, key=lambda k: get_distance(k, longitude, latitude))


def input_coordinate(message=''):
    try:
        return float(input(message))
    except ValueError:
        return None


def get_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        help='Ссылка для скачивания: https://devman.org/fshare/1503831681/4/'
    )
    args = parser.parse_args()
    return args


def get_bar_name(bar_dict):
    return bar_dict['properties']['Attributes']['Name']


if __name__ == '__main__':
    bars_filepath = parse_args().file_path
    try:
        bars = load_from_json(bars_filepath)['features']
    except FileNotFoundError:
        exit('Файл не найден')
    if bars is None:
        exit('Файл пуст')
    print('Чтобы найти ближайший бар укажите Ваши координаты')
    latitude = input_coordinate('Введите значение широты:')
    longitude = input_coordinate('Введите значение долготы:')
    if longitude is None or latitude is None:
        exit('Введены некорректные данные. Программа завершена')
    print('Самый большой бар:', get_bar_name(get_biggest_bar(bars)))
    print('Самый маленький бар:', get_bar_name(get_smallest_bar(bars)))
    print(
        'Ближайший к Вам бар:',
        get_bar_name(get_closest_bar(bars, longitude, latitude))
    )
