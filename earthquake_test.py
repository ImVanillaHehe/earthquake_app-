import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

start_time_in_json = input('Введите starttime: ')
end_time_in_json = input('Введите endtime: ')
latitude_in_json = input(": ")
longitude_in_json = input(': ')
max_radius_km_in_json = input(': ')

responced = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': start_time_in_json,
    'endtime': end_time_in_json,
    'latitude': latitude_in_json,
    'longitude': longitude_in_json,
    'maxradiuskm': max_radius_km_in_json
})

data = responced.json()

earthquake_list = data['features']
count = 0

if __name__ == "__main__":
    for earthquake in earthquake_list:
        count += 1
        print(f"{count}. Place: {earthquake['properties']['place']}")
