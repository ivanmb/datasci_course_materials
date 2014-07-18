from __future__ import division
import sys
import json
import operator

hash_count = {}


def process_hashtags(hashtags):
    for occur in hashtags:
        w = occur[u"text"]

        old_count = hash_count.get(w, 0)
        hash_count[w] = old_count + 1


def main():
    tweet_file = open(sys.argv[1])

    tweets = map(json.loads, tweet_file)
    tweets_tags = map(lambda t: t.get(u"entities", {}).get(u"hashtags", []), tweets)

    map(process_hashtags, tweets_tags)
    sorted_hashtags = sorted(hash_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    for i in range(0, min(10, len(sorted_hashtags))):
        word = sorted_hashtags[i][0]
        count = sorted_hashtags[i][1]
        print "%s %s" % (word.encode('utf-8'), count)

    if len(sorted_hashtags) < 10:
        for i in range(0, 10 - len(sorted_hashtags)): print ""


if __name__ == '__main__':
    main()
