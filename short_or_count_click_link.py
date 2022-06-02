import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def parse_link(url):
    parts = urlparse(url)
    return f"{parts.netloc}+ {parts.path}"


def shorten_link(url, token):
    header = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    params = {
        "long_url": url
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
    response.raise_for_status()
    response_list = response.json()
    return response_list['link']


def count_clicks(link, token):
    header = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    params = {
        "unit": "month"
    }
    link_id = parse_link(link)
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
        .format(link_id),
        params=params,
        headers=header)
    response.raise_for_status()
    response_list = response.json()
    return response_list['total_clicks']


def is_bitlink(url, token):
    header = {
        "Authorization": token
    }
    url_id = parse_link(url)
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url_id),
        headers=header)
    return response.ok


def main():
    load_dotenv()
    BITLY_TOKEN = os.getenv("access_token")
    url = input("Input the url: ")
    is_bitly_link = is_bitlink(url, BITLY_TOKEN)
    if is_bitly_link:
        try:
            counter = count_clicks(url, BITLY_TOKEN)
            print('Кликов', counter)
        except requests.exceptions.HTTPError:
            print("Can't get data from server")
    else:
        try:
            count_clicks = shorten_link(url, BITLY_TOKEN)
            print('Битлинк', count_clicks)
        except requests.exceptions.HTTPError:
            print("Can't get data from server")


if __name__ == '__main__':
    main()
