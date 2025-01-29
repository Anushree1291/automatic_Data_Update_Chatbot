import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()

# Access the keys
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
newsapi_key = os.getenv("NEWSAPI_KEY")

# Example: Setting up APIs with the keys
openai.api_key = openai_api_key

from google.cloud import vision
vision_client = vision.ImageAnnotatorClient.from_service_account_json(google_api_key)



def fetch_articles_from_api():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'technology',
        'apiKey': newsapi_key
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return [{"title": art['title'], "content": art['description']} for art in articles]

def fetch_articles_from_website():
    url = "https://example.com/articles"  # Replace with your source
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for article in soup.find_all('div', class_='article'):
        title = article.find('h2').get_text()
        content = article.find('p').get_text()
        articles.append({"title": title, "content": content})
    return articles
