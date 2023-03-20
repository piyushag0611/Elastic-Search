from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
import time
import copy
import hidden
import uuid
import json
import hashlib
import pandas as pd
from ast import literal_eval

movie_list = pd.read_csv("C:\\Spring Term\\Elastic Search\\archive\\movies_metadata.csv")

secrets = hidden.elastic()

es = Elasticsearch(
    [ secrets['host'] ],
    http_auth=(secrets['user'], secrets['pass']),
    url_prefix = secrets['prefix'],
    scheme=secrets['scheme'],
    port=secrets['port'],
    connection_class=RequestsHttpConnection,
)
indexname = secrets['user']

# Start fresh
# https://elasticsearch-py.readthedocs.io/en/master/api.html#indices
res = es.indices.delete(index=indexname, ignore=[400, 404])
print("Dropped index", indexname)
print(res)

res = es.indices.create(index=indexname)
print("Created the index...")
print(res)

for i in range(400):
    movie = movie_list.iloc[i]
    if(not movie['title']!=movie['title']):
        title_ = movie['title']
    else:
        continue
    if(not movie['tagline']!=movie['tagline']):
        tagline_ = movie['tagline']
    else:
        tagline_ = 'not available'
    genres_ = []
    if(movie['genres'] != '[]'):
        genre_list = literal_eval(movie['genres'])
        for item in genre_list:
            genres_.append(item['name'])
    
    if(not movie['overview']!=movie['overview']):
        overview_ = movie['overview']
    else:
        overview_ = 'not available'

    doc = {
        'title': title_,
        'tagline': tagline_,
        'overview': overview_,
        'genre' : genres_
    }
    
    res = es.index(index=indexname, id=movie['id'], body=doc)

    if i % 100 == 0 :
        print(i, 'loaded...')
        time.sleep(1)

res = es.indices.refresh(index=indexname)
print("Index refreshed", indexname)
print(res)


