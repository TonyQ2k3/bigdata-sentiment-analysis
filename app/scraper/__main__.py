import os
import sys
from scraper.twitter_scraper import Twitter_Scraper


try:
    from dotenv import load_dotenv
    print("Loading .env file")
    load_dotenv()
    print("Loaded .env file\n")
except Exception as e:
    print(f"Error loading .env file: {e}")
    sys.exit(1)


def main(
    max=10,
    query=None,
    ):
    USER_UNAME = os.environ['TWITTER_USERNAME']
    USER_PASSWORD = os.environ['TWITTER_PASSWORD']

    if USER_UNAME is not None and USER_PASSWORD is not None:
        scraper = Twitter_Scraper(
            username=USER_UNAME,
            password=USER_PASSWORD,
        )
        scraper.login()
        scraper.scrape_tweets(
            max_tweets=max,
            scrape_query=str(query),
        )
        dataframe = scraper.save_tweets()
        return dataframe
    else:
        print("Please provide a valid username and password")
        return None
    

if __name__ == "__main__":
    main()
