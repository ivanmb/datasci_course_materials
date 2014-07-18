from __future__ import division
import sys
import json

scores = {}
words_in_positive = {}
words_in_negative = {}
word_scores = {}


def get_word_sentiment(word):
    return scores.get(word, 0)


def process_text(text):
    words = text.split()
    positive = [w for w in words if get_word_sentiment(w) > 0]
    negative = [w for w in words if get_word_sentiment(w) < 0]
    rest = [w for w in words if get_word_sentiment(w) == 0]

    for w in rest:
        if len(positive):
            count = words_in_positive.get(w, 0)
            words_in_positive[w] = count + 1
        if len(negative):
            count = words_in_negative.get(w, 0)
            words_in_negative[w] = count + 1


def process_words():
    for w in words_in_positive.keys() + words_in_negative.keys():
        count_pos = words_in_positive.get(w, 0)
        count_neg = words_in_negative.get(w, 0)
        # Check to avoid divide by zero
        freq = count_pos / (count_neg if count_neg > 0 else 1)
        word_scores[w] = freq


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweets = map(json.loads, tweet_file)
    tweets_text = map(lambda t: t[u"text"] if u"text" in t else "", tweets)

    map(process_text, tweets_text)
    process_words()

    for word in word_scores:
        print "%s %s" % (word.encode('utf-8'), word_scores[word])


if __name__ == '__main__':
    main()
