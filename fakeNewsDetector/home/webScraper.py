# from .models import News    
from gnews import GNews
from bs4 import BeautifulSoup
import requests
from googletrans import Translator, constants
from pprint import pprint

def process_news_object(url, content):

    # print("Source URL:", url)
    # print("News Content:", content)
    # print()  # Print an empty line for separation

    # ... continue with your scraping code ...

    cleaned_content = content.replace('\r', '').replace('\n', '')
    clean_content=cleaned_content
    google_news = GNews()
    Similar_news = google_news.get_news(clean_content)
    
    if Similar_news:
        news = Similar_news[0]
        # print("Title : ", news["title"][:news["title"].rindex('-')], "\nPublisher : ", news["publisher"]["title"], "\nSource : ", news["url"])

        print("news URL : ", news['url'])
        
        code = requests.get(news['url'])
        soup = BeautifulSoup(code.text, "html.parser")
    
        print("\nDetails :")

        totalText = []
        for item in soup.find_all('p'):
            print(item.text)
            totalText.append(item.text)
            
        # for item in soup.find_all('span'):
        #     print(item.text)
        #     totalText.append(item.text)
        
        for item in soup.find_all('div'):
            print(item.text)
            totalText.append(item.text)
        

        # return soup.find_all('p')
        return totalText
