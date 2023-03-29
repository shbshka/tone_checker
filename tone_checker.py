from csv_reader import words_pos, words_neg


def count_words(text):
    pos_index = 0
    neg_index = 0
    for word in text:
        if word in words_pos:
            pos_index += 1
        if word in words_neg:
            neg_index += 1
    return pos_index, neg_index


def count_index(pos_index, neg_index):
    if pos_index > neg_index:
        print("The tone is positive")
    elif neg_index > pos_index:
        print("The tone is negative")
    elif pos_index == neg_index:
        print("The tone is neutral")

