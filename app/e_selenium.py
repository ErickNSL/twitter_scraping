    ### TWITTER SCRAPING ###

#INSTALLING THE DEPENDENCIES
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
from time import sleep


### Set-up driver/browser
### You need to install your own web driver, and put in the app folder to read it directly(firefox or safari etc.).
def setup_browser():
    driver= webdriver.Chrome()
    return driver


### Seting-up the Log-in
def log_in(driver, user, password):
    try:
        driver.get('https://twitter.com/i/flow/login')
        sleep(1)
        USER_NAME = user
        USER_PASWWORD = password
        user_name = driver.find_element(By.XPATH,"//input[@name='text']")
        user_name.send_keys(USER_NAME)
        next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
        next_button.click()
        sleep(1.5)
        user_password = driver.find_element(By.XPATH,"//input[@name='password']")
        user_password.send_keys(USER_PASWWORD)
        log_button = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
        log_button.click()
        sleep(2)
    except NoSuchElementException:
        sleep(1)
        user_name = driver.find_element(By.XPATH,"//input[@name='text']")
        user_name.send_keys(USER_NAME)
        next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
        next_button.click()
        sleep(2)





###Getting into Objetive profile
def Objetive(driver, at, not_at):
    try:
        sleep(1.5)
        search = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
        search.send_keys(at)
        endsearch = driver.find_element(By.XPATH,f"//span[contains(text(), '{not_at}')]")
        endsearch.click()
        sleep(3)
    except NoSuchElementException:
        sleep(1)
        search = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
        search.send_keys(at)
        endsearch = driver.find_element(By.XPATH,f"//span[contains(text(), '{not_at}')]")
        endsearch.click()
        sleep(3)
          


#Getting the the elements of a tweet
def scrape_tweets(driver):
    #Empty list to storage the data
    UserTags = []
    TimeSs = []
    Tweets = []
    Replys = []
    ReTweets = []
    Likes = []

    #Scroll values 1.0 = 100% 0.01 = 1%
    scroll = 0.0
    scroll_increment = random.uniform(0.02, 0.05)

    #Getting the tweet elements
    celltweet = driver.find_elements(By.XPATH, "//div[@data-testid='cellInnerDiv']")
    while True:
        sleep(1.4)
        for cell in celltweet:
            UserTag = driver.find_element(By.XPATH, ".//div[@data-testid='User-Name']").text
            UserTags.append(UserTag)
            TimeS = driver.find_element(By.XPATH, ".//time").get_attribute('datetime')
            TimeSs.append(TimeS)
            Tweet = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
            Tweets.append(Tweet + '///OTHER///')
            Reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
            Replys.append(Reply)
            ReTweet = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
            ReTweets.append(ReTweet)
            Like = driver.find_element(By.XPATH, ".//div[@data-testid='like']").text
            Likes.append(Like)
            
        
        #Scrolling the page/display scroll %
        print(scroll)
        scroll += scroll_increment
        driver.execute_script(f'window.scrollTo(0,document.body.scrollHeight *{scroll});')

        #set the number of results to brake the loop
        Tweetslen = list(set(Tweets))
        if len(Tweetslen) >= 10:
            break

    return UserTags, TimeSs, Tweets, Likes, Replys, ReTweets
    


