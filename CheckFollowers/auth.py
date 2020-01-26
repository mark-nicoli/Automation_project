from instapy import InstaPy
import time
import pickle
from InstagramAPI import InstagramAPI
from datetime import datetime

username = ''
pwd = ''
user_id  = ''

API = InstagramAPI(username,pwd)
API.login()

API.getUsernameInfo(user_id)
API.LastJson
followers   = []
next_max_id = True
while next_max_id:
    if next_max_id == True: next_max_id=''
    _ = API.getUserFollowers(user_id,maxid=next_max_id)
    followers.extend ( API.LastJson.get('users',[]))
    next_max_id = API.LastJson.get('next_max_id','')

followers = [dic['username'] for dic in followers]

following   = []
next_max_id = True
while next_max_id:
    if next_max_id == True: 
        next_max_id=''
    _ = API.getUserFollowings(user_id,maxid=next_max_id)
    following.extend ( API.LastJson.get('users',[]))
    next_max_id = API.LastJson.get('next_max_id','')

following = [dic['username'] for dic in following]

snakes = [x for x in following if x not in followers]
snakes.reverse()
print("\n".join(list(snakes)))
print("Amount of snakes: {}".format(len(snakes)))

API.logout()
