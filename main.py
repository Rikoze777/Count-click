import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='<Required> url link')
    return parser


def parse_link(url):
    parts = urlparse(url)
    return f"{parts.netloc}{parts.path}"


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
    bitly_token = os.environ.get("BITLY_TOKEN")
    parser = create_parser()
    url_link = parser.parse_args()
    url = url_link.url
    is_bitly_link = is_bitlink(url, bitly_token)
    if is_bitly_link:
        try:
            count_links = count_clicks(url, bitly_token)
            print('Количество переходов по ссылке битли', count_links)
        except requests.exceptions.HTTPError:
            print("Can't get click count")
    else:
        try:
            short_links = shorten_link(url, bitly_token)
            print(short_links)
        except requests.exceptions.HTTPError:
            print("The link is wrong")


if __name__ == '__main__':
    main()
