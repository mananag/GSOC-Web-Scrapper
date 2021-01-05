import pandas
import requests
from bs4 import BeautifulSoup


def after_2016():
    year_urls = []
    for year in range(2016, 2021):
        year_url = 'https://summerofcode.withgoogle.com/archive/' + str(year) + '/organizations/'
        r = requests.get(year_url)
        c = r.content

        soup = BeautifulSoup(c, "html.parser")
        cards = soup.find_all("a", {"class": "organization-card__link"})

        d = {'Organizations': [], 'About': [], 'Technology': [], 'Category': [], 'Topics': []}

        urls = []

        for card in cards:
            urls.append("https://summerofcode.withgoogle.com" + card.attrs['href'])
            d['Organizations'].append(card.find("h4").text)
            d['About'].append(card.find("div", {"class": "organization-card__tagline"}).text)

        for url in urls:
            temp = []
            r_temp = requests.get(url)
            s_temp = BeautifulSoup(r_temp.content, "html.parser")
            separator = ', '
            for tech in s_temp.find_all('li', {'class': 'organization__tag organization__tag--technology'}):
                temp.append(tech.text)
            d['Technology'].append(separator.join(temp))
            catag = s_temp.find('li', {'class': "organization__tag organization__tag--category"})
            d['Category'].append(catag.find('a').text)
            temp = []
            for tech in s_temp.find_all('li', {'class': 'organization__tag organization__tag--topic'}):
                temp.append(tech.text)
            d['Topics'].append(separator.join(temp))

        df = pandas.DataFrame(d)
        df
        df.to_csv('.//doc//gsoc' + str(year) + '.csv')


def before_2016():
    for year in range(2009, 2016):
        year_url = "https://www.google-melange.com/archive/gsoc/" + str(year)

        r = requests.get(year_url)
        c = r.content

        soup = BeautifulSoup(c, "html.parser")
        cards = soup.find_all("span", {"class": "mdl-list__item-primary-content"})

        d = {"Organizations": []}
        for card in cards:
            d["Organizations"].append(card.find("a").text)
        df = pandas.DataFrame(d)
        df
        df.to_csv('gsoc' + str(year) + '.csv')
