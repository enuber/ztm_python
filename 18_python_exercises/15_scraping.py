# Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library), but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

base_URL = 'https://www.nytimes.com/'
res = requests.get(base_URL)
soup = BeautifulSoup(res.text, 'html.parser')

# hub-game-card__name
story_titles = soup.select('.css-xdandi p')


def story_titles_cleaned(stories):
    stories_cleaned = []
    for index, story in enumerate(stories):
        stories_cleaned.append(story.getText())
        stories_links = stories[index].find_parent(
        ).find_parent().find_parent().get('href', None)
        print(story.getText())
        print(stories_links, '\n')
    return stories_cleaned


story_titles_cleaned(story_titles)
