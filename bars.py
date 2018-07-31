import json


def load_data(filepath):
    pass


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass



import json
import requests

#данные с сайта мос
api_key = 'cd3e37fff386243eb88f39065816dacf'
ref = 'https://apidata.mos.ru/v1/features/1796?api_key={}'.format(api_key)

data = requests.get(ref).json()
print(len(data['features']))
print(data['features'][0])

#запись json
with open ('bars.json', 'w') as f:
    json.dump(data,f)

#чтение json
with open('bars.json', 'r') as f:
    data = json.load(f)


#инфо по барам

data['features'][2]['properties']['Attributes']['Name']

bars = { x ['properties']['Attributes']['Name'] : x ['properties']['Attributes']['SeatsCount'] for x in data['features']}
 (min(bars, key=lambda k: bars[k]))
 (max(bars, key=lambda k: bars[k]))


print (data['features'][2]['geometry']['coordinates'])


x = input()
longitude, latitude = map(float, input().split())

import json
import requests
from math import sqrt
import argparse

#считывание инфы
def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data
#print (load_data('bars.json'))


def get_biggest_bar(data):
    biggest_bar = min(data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(data):
    smallest_bar = min(data['features'], key=lambda k: k['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']

def get_distance(bar, longitude, latitude):

    bar_long = bar['geometry']['coordinates'][0]
    bar_lat = bar['geometry']['coordinates'][1]
    return sqrt((bar_long - longitude)**2+(bar_lat-latitude)**2)

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
    #data = load_data(parse_args())
    data = load_data('bars.json')
    biggest = get_biggest_bar(data)
    smallest = get_smallest_bar(data)
    longitude, latitude = map(float, input().split())
    closest = get_closest_bar(data,longitude, latitude)
    print(closest)


