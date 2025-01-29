from transformers import pipeline
from multilingual import detect_language, translate
from embeddings import get_embeddings

# Initialize Hugging Face text-generation model
generator = pipeline("text-generation", model="gpt2")

# Supported languages
supported_languages = ["en", "es", "fr", "hi"]

def handle_query(user_query):
    """
    Handle user query and generate a response, supporting multilingual input.
    Args:
        user_query (str): The user's input query.
    Returns:
        str: Chatbot's response in the user's language.
    """
    # Detect language
    user_lang = detect_language(user_query)

    if user_lang not in supported_languages:
        return "Sorry, I do not support this language yet."

    # Translate to English if needed
    if user_lang != "en":
        user_query = translate(user_query, user_lang, "en")

    # Generate response in English
    response = generator(user_query, max_length=50, num_return_sequences=1)[0]["generated_text"]

    # Translate response back to user's language
    if user_lang != "en":
        response = translate(response, "en", user_lang)

    return response
