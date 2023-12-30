import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_fake_user_agent():
    ua = UserAgent()
    return ua.random

def extract_soup(url):
    headers = {
        'User-Agent': get_fake_user_agent(),
    }

    try:
        response = requests.get(url, allow_redirects=True, headers=headers)
        response.raise_for_status()

        final_url = response.url
        # print(final_url)

        
        final_response = requests.get(final_url, headers=headers)

        soup = BeautifulSoup(final_response.content, 'html.parser')
        
        return soup
    except soup.exceptions.RequestException as e:
        print(f'Error: {e}')
        return