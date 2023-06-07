# from .models import News    
from gnews import GNews
from bs4 import BeautifulSoup
import requests

def process_news_object(url, content):

    # print("Source URL:", url)
    # print("News Content:", content)
    # print(url)  # Print an empty line for separation

    # ... continue with your scraping code ...

    cleaned_content = content.replace('\r', '').replace('\n', '')
    clean_content=cleaned_content
    google_news = GNews()
    Indian_news = google_news.get_news(clean_content)
    if Indian_news:
        news = Indian_news[0]
        # print("Title : ", news["title"][:news["title"].rindex('-')], "\nPublisher : ", news["publisher"]["title"], "\nSource : ", news["url"])
        url_search = news['url']
    
        code = requests.get(url_search)
        soup = BeautifulSoup(code.text, "html.parser")
    
        print("\nDetails :")

        for item in soup.find_all('p'):
            print(item.text)

        return soup.find_all('p')
