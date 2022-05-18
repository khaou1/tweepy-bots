import tweepy 

consumer_key="PxKJuonUhVuyiE5KzcjazfrWR"
consumer_secret="xSl4Q1T6jfs5DqiseNeVJLsEpcfZpk5LjrBUpAJXebWd56aBIE"
access_token="1522356900204933120-NvVS8bZxeODCIESjbBWQ46iQNZlKYb"
access_token_secret="gVGo4GOxfJCvyQ7gOY1alqJzjrZz1RLJZeGs92wBaGHXL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

#Calling api
api = tweepy.API(auth)

#WOEID of city
woeid = 468739

#fetching the trends 
trends = api.get_place_trends(id = woeid)

trend_list = []

for x in trends:
    for trend in x["trends"]:
        trend_list.append(trend["name"])

open_string = "The top 10 trending for Buenos Aires today is: \n"
final_string = "\n".join(trend_list[:10])

api.update_status(open_string + final_string)

