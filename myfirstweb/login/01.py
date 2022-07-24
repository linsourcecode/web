
from redisbloom.client import Client
db  = Client(host="hadoop101",
                           port=6379,
                           # password=123,
                           db=0)
print(int(db.bfExists('userinfo', 'a')))
