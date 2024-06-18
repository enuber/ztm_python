# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

from bs4 import BeautifulSoup
import requests

# URL of the article
base_URL = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

# Fetch the content
res = requests.get(base_URL)
soup = BeautifulSoup(res.text, 'html.parser')

# Select the relevant parts of the article
article_title = soup.select_one('.ContentHeaderHed-NCyCC')
article_summary = soup.select_one('.ContentHeaderDek-bIqFFZ')
article_bylines = soup.select('.bylines__byline a')
article_date = soup.select_one('.ContentHeaderPublishDate-eIBicG')
article_paragraphs = soup.select('.body__inner-container p')

# Get the filename from the user
filename = input('What file name would you like to save the story to? ')

# Function to output the full story


def output_full_story(title, summary, bylines, date, story, filename):
    story_title = title.get_text() if title else 'No title found'
    story_summary = summary.get_text() if summary else 'No summary found'
    story_bylines = [byline.get_text() for byline in bylines]
    story_date = date.get_text() if date else 'No date found'
    story_paragraphs = [paragraph.get_text() for paragraph in story]

    with open(filename, mode='w') as file:
        file.write(story_title + '\n\n')
        file.write(story_summary + '\n\n')
        file.write(f"By {story_bylines[0] if len(
            story_bylines) > 0 else 'N/A'} \n\n")
        if len(story_bylines) > 1:
            file.write(f"Photography By {story_bylines[1]} \n\n")
        file.write(story_date + '\n\n')
        file.write(
            '________________________________________________________________________________\n\n')
        for paragraph in story_paragraphs:
            file.write(paragraph + '\n\n')


# Call the function to output the story
output_full_story(article_title, article_summary, article_bylines,
                  article_date, article_paragraphs, filename)
