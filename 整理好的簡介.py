import pymongo
MONGO_HOST = '10.2.14.10'
MONGO_DB = 'kingstone'
MONGO_COLLETION = 'clean_data'
from pymongo import MongoClient
#   http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=20180817&stockNo=2330

def connect_mongo():  #連線資料庫
    global collection
    client = MongoClient(MONGO_HOST, 27017)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLETION]

connect_mongo()  #呼叫連線資料庫函式
cursor = collection.find()  #依query查詢資料
df=  pd.DataFrame(list(cursor))  #轉換成DataFrame
del df['id']
df.head()
