# WEB SCRAPING
# you can go to a website like disneystore.com/robot.txt
# robots.txt tells you what you can and can't scrape.

# beautiful soup allows us to use the html and grab different data.
# requests allows us to download the initial html

import requests
from bs4 import BeautifulSoup

# requests first take the URL you want to grab
res = requests.get('https://news.ycombinator.com/news')
# this gives us the text (html) from this page. just res would give us the status 200
# print(res.text)

# convert it from string to something we can use
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup) # gives us the html itself instead of as a string
# print(soup.head)  # can use this to get different parts of the html doc

# gives us the contents in a list (ie [item1, item2]) with each item being one line fo the html
# print(soup.body.contents)

# print(soup.find_all('a')) # gives a list of all <a>
# print(soup.find('a')) # gives us the first <a> on the page

# print(soup.find(id='score_40585728')) # grab a specific item by it's ID
# create a list of all the class score elements
print(soup.find_all(class_='score'))
