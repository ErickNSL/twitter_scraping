from e_selenium import setup_browser,log_in,Objetive,scrape_tweets
import pandas as pd
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
#-MAIN APP- /SET LOGIN/OBJETIVE/NUMBER OF RESULTS ON (e_selenium FILE)
def main():
    #Setup this variables
    user = os.environ.get("TW_USER")
    password = os.environ.get("TW_PASSWORD")
    looking_up_at = 'eczachly'
    Not_at = 'Zach Wilson'

    driver = setup_browser()
    log_in(driver, user, password)
    Objetive(driver, looking_up_at, Not_at)

    #Data storage and dataframe
    scrape_tweets(driver)
    UserTagslen,Timeslen, Tweetslen, Likeslen, Replayslen,Retweetslen = scrape_tweets(driver)
    data = {
        "User Name":UserTagslen,
        "Date": Timeslen,
        "Tweets":Tweetslen,
        "Likes":Likeslen,
        "Comments":Replayslen,
        "ReTweets":Retweetslen
    }
    createdTime= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    df = pd.DataFrame(data)
    df.drop_duplicates(subset=["User Name", "Date", "Tweets","Likes","Comments","ReTweets"], keep="first", inplace=True)

    #Seting the filename
    filename = f'Twitterblock_{Not_at}{createdTime}.csv'
    df.to_csv(f'{filename}', index=False)


if __name__ == "__main__":
    main()







