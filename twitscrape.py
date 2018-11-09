from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='

#twitscrape's arguments use 'query' and 'filename' as strings. 'quantity' and 'timeout' are integers
#Keep in mind 'timeout' uses 'sleep' so .2 is an acceptable value.
def twitscrape(query, quantity, timeout, filename):
    query = 'u' + "'" + query + "'"
    url = base_url + query
    browser.get(url)
    time.sleep(1)
    body = browser.find_element_by_tag_name('body')
    for _ in range(quantity):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(timeout)
    tweets = browser.find_elements_by_class_name('tweet-text')
    allTweets = ''
    for tweet in tweets:
        print(tweet.text)
        curTweet = tweet.get_attribute('innerHTML')
        allTweets = allTweets + "\n" + curTweet
    soup = BeautifulSoup(allTweets, "html.parser")
    text = soup.get_text()
    with open(filename, "w", encoding='utf-8') as text_file:
        text_file.write(text)
#example:
#twitscrape('president',5,.2, "president.txt")
