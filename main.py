from os import link
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
data = BeautifulSoup(res.text, 'html.parser')
links = data.select('.storylink')
subtext = data.select('.subtext')


def create_new_list(links, subtext):
    scraped_data = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if(len(vote)):
            points = int(vote[0].getText().replace(' points', ''))
            scraped_data.append({'title': title, 'url': href})

    return scraped_data


print(create_new_list(links, subtext))
