import requests

def check_website(url):
    response = requests.get(url)
    print(f"Статус сайта {url}: {response.status_code}")


check_website("https://google.com")
