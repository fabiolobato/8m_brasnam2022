from pymongo import MongoClient
from tqdm import tqdm


print("Conectando à base de dados")

MONGO_HOST = 'mongodb://localhost:27017/'
MONGO_DB = 'SUA_DATABASE_AQUI'
MONGO_COLL = 'SUA_COLLECTION_AQUI'

client = MongoClient(MONGO_HOST)
db = client[MONGO_DB]
tweets = db[MONGO_COLL]

print(f'Base de dados: {db.name}\nCollection: {tweets.name}')

pipeline = [
    {
        '$group': {
            '_id': '$id',
            'uniqueIds': {
                '$addToSet': '$_id'
            },
            'count': {
                '$sum': 1
            }
        }
    }, {
        '$match': {
            'count': {
                '$gt': 1
            }
        }
    }, {
        '$sort': {
            'count': -1
        }
    }
]

print('Query iniciada: buscando documentos em duplicidade')
data = list(tweets.aggregate(pipeline, allowDiskUse=True))
print('Query finalizada')

print(f'Quantidade de documentos com registros duplicados: {len(data)}')

ids = [d2 for d in data for d2 in d['uniqueIds'][1:]]

print(f'Quantidade de documentos a serem excluídos: {len(ids)}')

for id in tqdm(ids):
    tweets.delete_one({'_id': id})

print("Exclusão de documentos finalizadas.")