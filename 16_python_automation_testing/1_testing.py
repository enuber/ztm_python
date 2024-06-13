# CANT GET SELENIUM To WORK SkIPPED SECTION

# Selenium with python
# https://selenium-python.readthedocs.io/

# to use selenium you must also use the drivers found under 1.5 drivers section on webpage
# chromedriver needs to bee in save folder as the python file

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')


print(chrome_browser)
