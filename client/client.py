import requests
import time

def request():
    while True: 
        time.sleep(1)
        r = requests.get('http://server:5000/test')
        print(r.text)

if __name__ == "__main__":
    print("starts")
    request()