import codecs
import json
import sys

def parse_json_tweet(line):
    tweet = json.loads(line)
    htags = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    urls = [url['expanded_url'] for url in tweet['entities']['urls']]
    return [htags, urls]
if __name__ == "__main__":
	file_timeordered_json_tweets = codecs.open("tweetsdata.txt", 'r', 'utf-8')
	fout1 = codecs.open("output_hashtags.txt", 'w','utf-8')
	fout2 = codecs.open("output_urls.txt", 'w','utf-8')
for line in file_timeordered_json_tweets:
    try:
        [htags,urls] = parse_json_tweet(line)
        fout1.write(str(htags) + "\n")
	fout2.write(str(urls) + "\n")
    except:
        pass

file_timeordered_json_tweets.close()
fout1.close()
fout2.close()
