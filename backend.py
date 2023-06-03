import requests 
API_KEY = '65c33b6ed2fb82d5db24b143ad971410'

def get_data(place,days,option):
    urls = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url=urls)
    data = response.json() 
    filtered_data = data['list']
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    if option == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if option == 'Sky':
        filtered_data = [data['weather'][0]['main'] for dict in filtered_data]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place='Tokyo',days=2,option='Temperature'))   