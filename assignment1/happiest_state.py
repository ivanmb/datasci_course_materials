import sys
import json
import operator

states_by_code = {
    'ak': 'alaska',
    'al': 'alabama',
    'ar': 'arkansas',
    'as': 'american samoa',
    'az': 'arizona',
    'ca': 'california',
    'co': 'colorado',
    'ct': 'connecticut',
    'dc': 'district of columbia',
    'de': 'delaware',
    'fl': 'florida',
    'ga': 'georgia',
    'gu': 'guam',
    'hi': 'hawaii',
    'ia': 'iowa',
    'id': 'idaho',
    'il': 'illinois',
    'in': 'indiana',
    'ks': 'kansas',
    'ky': 'kentucky',
    'la': 'louisiana',
    'ma': 'massachusetts',
    'md': 'maryland',
    'me': 'maine',
    'mi': 'michigan',
    'mn': 'minnesota',
    'mo': 'missouri',
    'mp': 'northern mariana islands',
    'ms': 'mississippi',
    'mt': 'montana',
    'na': 'national',
    'nc': 'north carolina',
    'nd': 'north dakota',
    'ne': 'nebraska',
    'nh': 'new hampshire',
    'nj': 'new jersey',
    'nm': 'new mexico',
    'nv': 'nevada',
    'ny': 'new york',
    'oh': 'ohio',
    'ok': 'oklahoma',
    'or': 'oregon',
    'pa': 'pennsylvania',
    'pr': 'puerto rico',
    'ri': 'rhode island',
    'sc': 'south carolina',
    'sd': 'south dakota',
    'tn': 'tennessee',
    'tx': 'texas',
    'ut': 'utah',
    'va': 'virginia',
    'vi': 'virgin islands',
    'vt': 'vermont',
    'wa': 'washington',
    'wi': 'wisconsin',
    'wv': 'west virginia',
    'wy': 'wyoming'
}

states_by_name = {v: k for k, v in states_by_code.items()}

word_scores = {}
state_sentiment = {}


def get_tweet_state(tweet):
    # Place can be present and be None, as well as not be present
    place = tweet.get("place", None)
    state = None

    if place is not None:
        place_name = place.get("name", "").lower()
        state = states_by_name.get(place_name, None)

    #If still didn' find a state, try to check on user's location
    if state is None:
        location = tweet.get("user", {}).get("location", "")

        state_codes = filter(lambda t: t.lower() in states_by_code.keys(), location.split())
        state_names = filter(lambda t: t.lower() in states_by_name.keys(), location.split())

        # If state code found, use it.
        if len(state_codes):
            state = state_codes[0].lower()
        # If state name found, use it. Else, still None
        elif len(state_names):
            state_name = state_names[0].lower()
            state = states_by_name[state_name]

    return state


def get_word_sentiment(word):
    return word_scores.get(word, 0)


def process_tweet(tweet):
    text = tweet.get("text", "")
    # Split tweet text into words
    words = text.split()
    # Weight words by its sentiment
    word_weights = map(get_word_sentiment, words)
    # Tweet's sentiment is the sum of its words sentiments
    tweet_sentiment = sum(word_weights)
    # Try to assign a state to the tweet
    tweet_state = get_tweet_state(tweet)

    if tweet_state is not None:
        state_sentiment[tweet_state] = state_sentiment.get(tweet_state, 0) + tweet_sentiment


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        word_scores[term] = int(score)  # Convert the score to an integer.

    tweets = map(json.loads, tweet_file)
    map(process_tweet, tweets)

    print max(state_sentiment.iteritems(), key=operator.itemgetter(1))[0].upper()


if __name__ == '__main__':
    main()
