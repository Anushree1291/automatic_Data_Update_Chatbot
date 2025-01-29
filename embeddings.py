import openai
import os
from dotenv import load_dotenv
from google.cloud import vision
from transformers import AutoTokenizer, AutoModel
import torch
load_dotenv()

# Access the keys
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
newsapi_key = os.getenv("NEWSAPI_KEY")

service_account_json_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


vision_client = vision.ImageAnnotatorClient.from_service_account_json(service_account_json_path)


openai.api_key = openai_api_key


# Instantiate the Vision API client



# Load a Hugging Face model for embeddings (e.g., 'sentence-transformers/all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Function to generate embeddings
def get_embeddings(texts):
    """
    Generate embeddings for a list of texts.
    Args:
        texts (list): List of strings to generate embeddings for.
    Returns:
        list: List of embeddings as PyTorch tensors.
    """
    with torch.no_grad():
        tokens = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**tokens)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Average pooling
    return embeddings.tolist()
