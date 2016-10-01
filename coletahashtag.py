# Instale o tweepy, caso ainda nao o tenha.
#   pip install tweepy
import tweepy


consumer_key="VL1j9NRdaAOjtVYRtWQGfPBcJ"
consumer_secret="6k9W95UAIhmsHyNFps7Gcu1yCeWI1iFZNdvLZOvq1vUK2KlUI7"
access_token="14147108-KM4oIdiORvMkolmhLk2f5ym8txnwkcnbVqAWpS3Ki"
access_token_secret="ezBfBHrmePXWcEUQEjTHXXfIJ0AtqkrdSVKmNY9DNb0Ht"


# # Registre sua aplicacao em https://apps.twitter.com
# consumer_key="PONHA-SUA-CONSUMER-KEY-AQUI"
# consumer_secret="PONHA-SUA-CONSUMER-SECRET-AQUI"
# access_token="PONHA-SEU-ACCESS-TOKEN-AQUI"
# access_token_secret="PONHA-SEU-ACCESS-TOKEN-SECRET-AQUI"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# http://tweepy.readthedocs.io/en/v3.5.0/api.html#API.search
# https://dev.twitter.com/rest/reference/get/search/tweets
# https://github.com/tweepy/tweepy/blob/master/tweepy/api.py#L1207
tweets = api.search(q='#vemprarua')

i = 1
while tweets:
	for tweet in tweets:
		print('%d, %d, %s, %-20s, %s' % (i, tweet.id, tweet.created_at, tweet.author.screen_name, tweet.text))
		i += 1


	last_id = tweet.id
	tweets = api.search('#vemprarua',max_id=last_id-1)
