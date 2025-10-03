import requests

response = requests.get("https://api.github.com")

print(response)          # فقط وضعیت (status code و نوع)
print(response.status_code)  # کد وضعیت مثل 200
# print(response.json())       # محتوای پاسخ (خود داده‌ها به صورت دیکشنری)
print(response.status_code)

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

import requests
from requests.exceptions import HTTPError

URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")