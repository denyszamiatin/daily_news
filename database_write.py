from pymongo import MongoClient
from settings import MONGODB_SERVER, MONGODB_PORT, MONGODB_DB, MONGODB_COLLECTION


class SaveToMDB:
    def __init__(self):
        self.client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
        self.db = self.client[MONGODB_DB]
        self.collection = self.db[MONGODB_COLLECTION]


class InsertData:
    def __init__(self, title, text, link, date):
        self.title = title
        self.text = text
        self.link = link
        self.date = date

    def to_dict(self):
        return {"title": self.title,
                "text": self.text,
                "link": self.link,
                "date": self.date}


save_to_mdb = SaveToMDB()


def insert(dict):
    return save_to_mdb.collection.insert_one(dict).inserted_id