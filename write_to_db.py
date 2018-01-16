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
'''
title = 'World Bank speaks up against Ukraine’s current bill on anti-graft court: $800 mln at stake'
text = 'If Ukraine is interested in securing World Bank’s guarantees worth $800 million the authorities should reconsider the draft law on High Anti-Corruption Court and ensure it is in line with the recommendations provided by the Venice Commission, that’s according to a letter to Rada Speaker Andriy Parubiy and Head of Poroshenko Administration Ihor Rainin signed off by Satu Kahkonen, World Bank’s Country Director Belarus, Moldova and Ukraine Europe and Central Asia published by Europeiska Pravda. REUTERS “The draft law [on HACC, submitted by President Poroshenko,] requires the following revisions to bring it into alignment with the recommendations of the Venice Commission and satisfy the requirements of the World Bank’s estimated $800 million Policy-Based Guarantee (PBG) to support key reforms in Ukraine," the letter says, according to EP. For the World Bank to unblock its financial assistance, Ukrainian authorities are strongly encouraged to make “a revision of the draft Law to align the jurisdiction of the HACC with the jurisdiction of NABU [National Anti-corruption Bureau of Ukraine] and SAPO [Special Anti-corruption Prosecutor’s Office],” which was actually one of the key recommendations of the Venice Commission. Read also Poroshenko administration responds to IMF criticism of antigraft court bill As UNIAN reported earlier, Ukraine had already seen a similar criticism of the said bill on the part of the International Monetary Fund. In a letter to Mr Rainin, the IMF’s resident representative in Ukraine informed that the passing of the current version of the HACC draft law would mean that Kyiv violated its obligations before its international partners.'
link = 'https://www.unian.info/detail/all_news'
date = '2017.12.31'

news_data = NewsData()
news_data.insert(title, text, link, date)
'''