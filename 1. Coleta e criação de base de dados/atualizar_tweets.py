import math
import time
import tweepy
from pymongo import MongoClient


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


MONGO_HOST = 'mongodb://localhost:27017/'
MONGO_DB = 'SUA_DATABASE_AQUI'
MONGO_COLL_ORIGEM = 'SUA_COLLECTION_DE_ORIGEM_AQUI'
MONGO_COLL_DESTINO = 'SUA_COLLECTION_DE_DESTINO_AQUI'

client = MongoClient(MONGO_HOST)
db = client[MONGO_DB]
collection = db[MONGO_COLL_ORIGEM]
collection2 = db[MONGO_COLL_DESTINO]

num_docs = collection.count_documents({})
num_limit = 1000
num_skip = 0
print(f"Documentos presentes na base: {num_docs}")


num_page = 0
pages = math.ceil(num_docs/num_limit)


print('Atualização de tweets iniciada')
print(f'{time.asctime(time.localtime(time.time()))}')

while num_page < pages:
    print(f'\nBloco {num_page + 1}/{pages}')

    docs = []
    tweets_ids = []

    docs = list(collection.find({}, {'id': True}
                                ).limit(num_limit).skip(num_skip))
    tweets_ids = [doc['id'] for doc in docs]

    print(f'Extraindo {len(tweets_ids)} tweets para atualização\n')

    data_to_update = {}
    data = []
    key = 0

    for tweet_id in tweets_ids:
        data.append(tweet_id)
        data_to_update[key] = data
        if(len(data) == 100):
            key = key + 1
            data = []

    for d in data_to_update.keys():
        updated_tweets = []
        tweets = []

        updated_tweets = api.statuses_lookup(
            data_to_update[d], tweet_mode='extended')
        tweets = [ut._json for ut in updated_tweets]
        collection2.insert_many(tweets)

        num_skip = num_skip + len(data_to_update[d])

        print(
            f'{len(data_to_update[d])} tweets enviados | {len(tweets)} atualizados | Total enviado: {num_skip}/{num_docs} | {(num_skip*100)/num_docs:.2f}%')

    num_page = num_page + 1

print('Atualização de tweets finalizada')
print(time.asctime(time.localtime(time.time())))