import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 
consumer_key="LRGd3TJ6VuUwOM0HJcFeOl0WM"
consumer_secret="lizN5xFqENDMvShWaSQUp6CuuGuQPazXuoJxUmGhChzY7D4bGT"
access_key="2269876512-xdLeXi7N1Slm9hdTr2FpqUWh9fZd9DxR7DeEC60"
access_secret="O5YSXFJz4IfHRzCzPX5sOGUWhE4ev3rWYmSwVaCVxZXu7"

# Function to extract tweets 
def get_tweets(username): 
		print(username)
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 200 tweets to be extracted 
		number_of_tweets=2
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		tmp=[] 

		# create array of tweet information: username, 
		# tweet id, date/time, text 
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		for j in tweets_for_csv: 

			# Appending tweets to the empty array tmp 
			tmp.append(j) 

		# Printing the tweets 
		# print(tmp) 
		test = api.followers(screen_name=username) 
		for j in test: 
			print(j.name) 



        


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("BeingSalmanKhan") 
