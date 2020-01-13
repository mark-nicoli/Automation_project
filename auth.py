from InstagramAPI import InstagramAPI

api = InstagramAPI("mark_nicoli19", password)
api.login
users_list = []

def getLikes(username):
    api.login()
    api.searchUsername(username)
    result = api.LastJson
    username_id = result['user']['pk']
    user_Posts = api.getUserFeed(username_id)
    result = api.LastJson
    media_id = result['items'][0]['id']
    api.getMediaLikers(media_id)
    users = api.LastJson
    for users in users:
        users_list.append({'pk':users['pk'], 'username':user['username']})
