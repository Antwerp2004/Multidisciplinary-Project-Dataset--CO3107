import requests
import matplotlib.pyplot as plt

AIO_USERNAME = "toan_fi"
AIO_KEY      = "aio_KLuE16UjOOOyQmmjNf8W37ylj7xl"



# url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_KEY}/data"
feed_url = 'https://io.adafruit.com/api/v2/toan_fi/feeds'
headers = {"X-AIO-Key": AIO_KEY, }

response = requests.get(feed_url, headers=headers)
response = response.json()

keys = []
for i in range(len(response)):
    keys.append(response[i]['key']) if response[i]['key'] != 'default' else None


def display(option, start_date = None, end_date = None, limit=1e9): #950 years
    if option == 'humid':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/display-humid/data?'
    elif option == 'temp':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/display-temp/data?'
    elif option == 'light':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/display-light/data?'
    count = False
    if start_date:
        url += ('&' if count else '' ) + f'start_time={start_date}'
        count = True
    if end_date:
        url += ('&' if count else '' ) + f'end_time={end_date}'
        count = True
    if limit:
        url += ('&' if count else '' ) + f'limit={limit}'
        count = True
    print(url)
    response = requests.get(url, headers=headers)
    response = response.json()
    data = []
    for i in range(len(response)):
        data.append((response[i]['value'],response[i]['created_at']))
    data = sorted(data, key=lambda x: x[1])
    return data
    
def control(option, value=None):
    if option == 'humid':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/control-humid/data'
    elif option == 'temp':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/control-temp/data'
    elif option == 'light':
        url = f'https://io.adafruit.com/api/v2/toan_fi/feeds/control-light/data'
    if value is None:
        current_value = requests.get(url, headers=headers).json()[0]['value']
        print(f"Current {option} value: {current_value}")
        return current_value
    value = min(max(value, 0), 100)
    payload = {'value': value}
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code


def toggle_lights():
    # Fetch the current light state
    url_get = f'https://io.adafruit.com/api/v2/toan_fi/feeds/control-light/data'
    response_get = requests.get(url_get, headers=headers)
    
    if response_get.status_code != 200:
        print("Failed to fetch current light status:", response_get.status_code)
        return response_get.status_code
    
    # Parse the current state
    current_state = response_get.json()[0]['value']
    # Send the new state
    new_state = 'off' if current_state == 'on' else 'on'
    payload = {'value': new_state}
    response_post = requests.post(url_get, headers=headers, json=payload)
    
    if response_post.status_code == 200:
        print(f"Light toggled successfully. New state: {new_state}")
    else:
        print("Failed to toggle light:", response_post.status_code)
    
    return response_post.status_code


# control('humid', 0)
control('temp', 0)