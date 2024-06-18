# WEB SCRAPING
# scrapy - another framework to scrape websites.
# beautiful soup - is a library so smaller than scrapy

# pprint helps with loo in console for printing something
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.find(id='score_40585728'))  # grab a specific item by it's ID
# print(soup.find_all(class_='score')) # create a list of all the class score elements

# print(soup.select('.score')) # grabs all the class='score'

# these links and votes are together so links[0] matches votes[0]
links = soup.select('.titleline')
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    # we use enumerate because we need the index. this allows us to then grab from subtext the correct item because it is based on the same order so index would work for both.
    for index, item in enumerate(links):
        title = links[index].getText()
        # second argument is default if there is not an href (ERROR IN HACKER NEWS PROJECT)
        href = links[index].find('a').get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


items = create_custom_hn(mega_links, mega_subtext)
pprint.pprint(items)
