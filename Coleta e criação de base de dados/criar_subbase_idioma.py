import json
from pymongo import MongoClient


# configurar conexão com a base de dados
MONGO_HOST = 'mongodb://localhost:27017/'
MONGO_DB_ORIGEM = 'SUA_DATABASE_DE_ORIGEM_AQUI'
MONGO_DB_DESTINO = 'SUA_DATABASE_DE_DESTINO_AQUI'
MONGO_COLL_ORIGEM = 'SUA_COLLECTION_DE_ORIGEM_AQUI'
MONGO_COLL_DESTINO = 'SUA_COLLECTION_DE_DESTINO_AQUI'

# server
client = MongoClient(MONGO_HOST)

# Database e collection de origem
db = client[MONGO_DB_ORIGEM]
tweets_origem = db[MONGO_COLL_ORIGEM]

# database e collection de destino
# P.S: se estes não existirem, eles serão criados
db2 = client[MONGO_DB_DESTINO]
tweets_destino = db2[MONGO_COLL_DESTINO]

# siglas seguem o padrão ISO 639-1
# para mais informações, consultar https://pt.wikipedia.org/wiki/ISO_639
sigla_idioma = 'pt'

# pipeline aggregation
pipeline2 = [
    {
        '$match': {
            'lang': sigla_idioma
        }
    }, {
        '$skip': 0
    }, {
        '$limit': 100000
    }
]

# selecionar os dados e inseri-los na nova database e/ou collection
data = list(tweets_origem.aggregate(pipeline2, allowDiskUse=True))
while len(data) > 0:
    print(f'{len(data)} documentos selecionados')
    tweets_destino.insert_many(data) 
    print(f'{len(data)} documentos inseridos')
    pipeline2[1]['$skip'] += 100000
    data = list(tweets_origem.aggregate(pipeline2, allowDiskUse=True))