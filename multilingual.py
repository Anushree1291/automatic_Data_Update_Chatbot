from langdetect import detect
from transformers import pipeline, MarianMTModel, MarianTokenizer

# Load translation models
translation_models = {
    "en-es": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es"),
    "es-en": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-es-en"),
    "en-fr": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
    "fr-en": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-fr-en"),
    "en-hi": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-hi"),
    "hi-en": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-hi-en"),
}

translation_tokenizers = {
    key: MarianTokenizer.from_pretrained(model_name)
    for key, model_name in {
        "en-es": "Helsinki-NLP/opus-mt-en-es",
        "es-en": "Helsinki-NLP/opus-mt-es-en",
        "en-fr": "Helsinki-NLP/opus-mt-en-fr",
        "fr-en": "Helsinki-NLP/opus-mt-fr-en",
        "en-hi": "Helsinki-NLP/opus-mt-en-hi",
        "hi-en": "Helsinki-NLP/opus-mt-hi-en",
    }.items()
}

# Function to detect language
def detect_language(text):
    return detect(text)

# Function to translate text
def translate(text, src_lang, tgt_lang):
    model_key = f"{src_lang}-{tgt_lang}"
    if model_key not in translation_models:
        raise ValueError(f"Translation from {src_lang} to {tgt_lang} not supported.")
    model = translation_models[model_key]
    tokenizer = translation_tokenizers[model_key]
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
