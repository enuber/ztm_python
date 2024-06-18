# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http: // www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

# This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.


from bs4 import BeautifulSoup
import requests

base_URL = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
res = requests.get(base_URL)
soup = BeautifulSoup(res.text, 'html.parser')

article_title = soup.select('.ContentHeaderHed-NCyCC')
article_summary = soup.select('.ContentHeaderDek-bIqFFZ')
article_bylines = soup.select('.bylines__byline a')
article_date = soup.select('.ContentHeaderPublishDate-eIBicG')
article_paragraphs = soup.select('.body__inner-container p')


def show_full_story(title, summary, bylines, date, story):
    story_bylines = []
    story_paragraphs = []
    story_title = title[0].getText()
    story_summary = summary[0].getText()
    for byline in bylines:
        story_bylines.append(byline.getText())
    story_date = date[0].getText()
    for paragraph in story:
        story_paragraphs.append(paragraph.getText())
    print(story_title, '\n')
    print(story_summary, '\n')
    print(f'By {story_bylines[0]} \nPhotogrpahy By {story_bylines[1]} \n')
    print(story_date, '\n')
    for paragraph in story_paragraphs:
        print(paragraph, '\n')


show_full_story(article_title, article_summary,
                article_bylines, article_date, article_paragraphs)
