from textblob import TextBlob 
import wikipedia

def search_wikipedia(name):
    """searchingwikipedia"""
    
    print(f"searching for name{name}")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """summarizing wikipedia"""

    print(f"summarizing for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """getting text blob object"""

    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """find wikipedia name and return phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases

    return phrases