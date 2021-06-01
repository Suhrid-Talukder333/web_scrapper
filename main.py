from os import link
import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/')
data = BeautifulSoup(res.text, 'html.parser')
links = data.select('.storylink')
subtext = data.select('.subtext')


def sort_by_vote(arr):
    return sorted(arr, key=lambda k: k['vote'])


def create_new_list(links, subtext):
    scraped_data = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if(len(vote)):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                scraped_data.append(
                    {'title': title, 'url': href, 'vote': points})
    return sort_by_vote(scraped_data)


pprint.pprint(create_new_list(links, subtext))
