import yaml
from pymongo import MongoClient

client = MongoClient()
db = client['quote_gun']
collection = db['quotes']
cursor = collection.find()
documents = list(cursor)

with open('all_quotes.yml', 'w') as fp:
    yaml.safe_dump(documents, fp, allow_unicode=True)

client.close()