import tone_checker
from pdftotext import extract_text_from_pdf
from lemmatizer import Lemmatize
from tone_checker import count_words, count_index

text = extract_text_from_pdf("D://Desktop/resume.pdf")['content'].split(" ")
tl = Lemmatize()

new_text = tl.normalize_document(text)
new_text = tl.remove_stop_words(new_text)

pos_index, neg_index = tone_checker.count_words(new_text)
tone_checker.count_index(pos_index, neg_index)











