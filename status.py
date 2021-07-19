import requests
import time

zahtev = requests.get("https://comtradeqa.herokuapp.com/")

print(zahtev.status_code)
time.sleep(10)