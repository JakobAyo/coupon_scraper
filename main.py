from scraping_logics import *
from request_handler import requests as rh

def main(website_name):
    url_website1 = f'https://www.gutegutscheine.de/search/{website_name}' # gutscheine.de
    url_website2 = f'https://gutscheine.focus.de/search?query={website_name}' # focus.de
    url_website3 = f'https://gutscheine.bild.de/suche?q={website_name}' # bild.de
    url_website4 = f'https://www.mydealz.de/gutscheine/search?query={website_name}' # mydealz.de
    url_website5 = f'https://gutscheine.computerbild.de/suchergebnisse?q={website_name}' # computerbild.de
    url_website6 = f'https://www.gutscheinsammler.de/suche?q={website_name}' # gutscheinsammler.de

    rh.extract_soup(url_website1)
    rh.extract_soup(url_website2)
    rh.extract_soup(url_website3)
    rh.extract_soup(url_website4)
    rh.extract_soup(url_website5)
    rh.extract_soup(url_website6)

main('defshop')