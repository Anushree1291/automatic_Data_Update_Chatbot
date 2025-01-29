import schedule
import time
from fetch_data import fetch_articles_from_api
from embeddings import get_embeddings
from vector_database import VectorDatabase

# Initialize the vector database
vector_db = VectorDatabase()

def update_knowledge_base():
    print("Fetching new data...")
    articles = fetch_articles_from_api()
    embeddings = get_embeddings([article['content'] for article in articles])
    vector_db.add_embeddings(embeddings, articles)
    print(f"Added {len(articles)} new articles to the database.")

# Schedule updates every hour
schedule.every(1).hours.do(update_knowledge_base)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
