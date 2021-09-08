import tweepy
import time

consumer_key = "tttqQhwfKVJTFGcaShTn1XKcX"
consumer_secret = "XDXGWkYZqnS8fAuEGAJKiWPLWssikBXe4NJIdm3Z8hq0srRt7O"

key = "2751985813-czmcYZQxWOFsInxNqomQYulHCdzzutzTcmdCc62"
secret = "coXuV3nGOQJdPQNNq9vHJq1zhFALCaTf0wsKGlwfkNFxG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE = "last_seen.txt"


def retrieve_id(file):
    file_read = open(file, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_id(id, file):
    file_write = open(file, "w")
    file_write.write(str(id))
    file_write.close()
    return


def reply():
    last_Seen_id = retrieve_id(FILE)
    mentions = api.mentions_timeline(last_Seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(mention.id)
        last_Seen_id = mention.id
        store_id(last_Seen_id, FILE)
        api.create_favorite(mention.id)
        api.update_status(
            '@' + mention.user.screen_name + ' Sorry, Ibrahim is not here today. This is the Robot System. Ibrahim will see your tweet soon. Thank you',
            mention.id)


while True:
    reply()
    time.sleep(15)
