import re
from collections import defaultdict
from string import punctuation
import spacy
from nltk.tokenize import sent_tokenize

nlp = spacy.load('en_core_web_sm')


def preprocess_text(text: str) -> str:
    # Remove extra whitespace and normalize text
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def score_sentences(text: str) -> dict:
    # Tokenize into sentences and score based on word frequency
    sentences = sent_tokenize(text)
    word_freq = defaultdict(int)
    
    doc = nlp(text.lower())
    for token in doc:
        if token.text not in punctuation and not token.is_stop:
            word_freq[token.text] += 1

    scores = {}
    for sentence in sentences:
        for word in sentence.lower().split():
            if word in word_freq:
                scores[sentence] = scores.get(sentence, 0) + word_freq[word]
    return scores


def summarize_text(text: str, summary_size: int = 3) -> list[str]:
    text = preprocess_text(text)
    scores = score_sentences(text)

    # Sort sentences by score and select top N
    sorted_sentences = sorted(
        scores.keys(),
        key=lambda x: scores[x],
        reverse=True
    )[:summary_size]

    return sorted_sentences
