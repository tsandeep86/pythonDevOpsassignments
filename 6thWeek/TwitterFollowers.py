
import tweepy

auth = tweepy.OAuthHandler("nCb9oDoCLtuVz9MQf5KvoIt3r", "w8sur9lNdsFTeCmrwJB1Jh3eK03Zby2NTLUKwiYyAznnECtggt")
# Redirect user to Twitter to authorize
#redirect_user(auth.get_authorization_url())
# Get access token
auth.set_access_token("112860257-tjvpXkGWz69jhOSvX1AUwVupjrNsPZjpajz4tsXs","5FgpF3VzyqP26SYNnqJejsMB0KobZQuXbdc4QXhVUXRXK")
# Construct the API instance
api = tweepy.API(auth)

#print tweepy.Cursor(api.followers, screen_name="tsandeep86").items()
users=tweepy.Cursor(api.followers, screen_name="swathygoru",count=200).items()

for foll in users:
    print foll.screen_name