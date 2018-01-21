from pymongo import MongoClient
class NewsData():
   def __init__(self, coll_name):
       client = MongoClient('localhost', 27017)
#        print(client.nodes)
       db = client['news_ch']
       self.collection = db[coll_name]
   def insert(self, title, text, link, date):
       return self.collection.insert_one({"title": title,
       "text": text,
       "link": link,
       "date": date}).inserted_id