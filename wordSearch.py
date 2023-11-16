import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    search_bar = '440 200' # x y

    query = input('What word do you want to find the definition of: ')
    search_query = f'what is the definition of {query}'

    device.shell('input keyevent 64')

    time.sleep(0.25) # wait for browser to load

    device.shell(f'input tap {search_bar}')

    device.shell(f'input text "{search_query}"') # make sure you have the quotation marks around your text
    device.shell('input keyevent 66')

    time.sleep(3) # wait for results to load