from __future__ import division
import sys
import json

word_count = {}


def count_words(text):
    words = text.split()
    for w in words:
        count = word_count.get(w, 0)
        word_count[w] = count + 1


def main():
    tweet_file = open(sys.argv[1])
    tweets = map(json.loads, tweet_file)
    tweets_text = map(lambda t: t[u"text"] if u"text" in t else "", tweets)

    map(count_words, tweets_text)
    total = sum(word_count.values())
    for word in word_count.keys():
        print "%s %s" % (word.encode('utf-8'), word_count[word] / total)


if __name__ == '__main__':
    main()
