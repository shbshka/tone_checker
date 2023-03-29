from nltk.corpus import stopwords
import pymorphy2
import re
from autocorrect import Speller


class Lemmatize:
    def __init__(self):
        self.parser = pymorphy2.MorphAnalyzer()

    def normalize_document(self, text):
        new_text = []
        for word in text:
            new_word = re.sub("[^A-z]", "", word)
            new_text.append(new_word)
        return new_text

    def remove_stop_words(self, new_text):
        stopwords_eng = stopwords.words("english")
        for word in new_text:
            if word and word in stopwords_eng:
                new_text.remove(word)
        return new_text

    def normalize_text(self, new_text):
        tokens = []
        for word in new_text:
            word = self.parser.normal_forms(word)[0]
            tokens.append(word)
        spelled_tokens = []
        for word in tokens:
            spell = Speller(lang="en")
            spelled_tokens.append(spell(word))
        return spelled_tokens




