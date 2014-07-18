import sys
import json

scores = {}


def get_word_sentiment(word):
    return scores.get(word, 0)


def calc_text_sentiment(text):
    words = text.split()
    word_weights = map(get_word_sentiment, words)
    print sum(word_weights)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweets = map(json.loads, tweet_file)
    tweets_text = map(lambda t: t[u"text"] if u"text" in t else "", tweets)
    map(calc_text_sentiment, tweets_text)


if __name__ == '__main__':
    main()
