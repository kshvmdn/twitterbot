import tweepy
from keys import *


class TwitterBot:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message, mention_id=None):
        self.api.update_status(status=message, mention_id=mention_id)

    def respond(self, mention_text, message):
        for mention in self.api.mentions_timeline(count=5):
            if mention_text in mention.text.lower():
                self.tweet(message.format(mention.user.screen_name), mention.id)
                self.api.create_favorite(mention.id)
                print('responded to {0}'.format(mention.user.screen_name))

if __name__ == "__main__":
    user = TwitterBot()
    user.respond('happy birthday', '{0} thanks!')
