#from pyfacebook import GraphAPI
import urllib3
import facebook as fb 
import requests

app_id='318341643486196'
app_secret='2ba2855f0c4e3baab0bf971123477659'
graph = fb.GraphAPI()
access_token = graph.get_app_access_token(app_id, app_secret)
graph = fb.GraphAPI(access_token=access_token)

#print(graph.get_object(id="10221877743276286"))
events = graph.request('/10221877743276286/friends')
#events = graph.request('/10221877743276286/posts')
#vents = graph.request('/me')
user = graph.get_object(id="10221877743276286")['name'] 
#print('User is - ', user)
#profile = graph.get_object(user)
#print('profile is - ', profile)
count = 6
query_string = 'posts?limit={0}'.format(count)
posts = graph.get_connections('10221877743276286', query_string)
print(posts)

#eventList = events['data']
#eventid = eventList[1]['id']
#event1 = graph.get_object(id=eventid,
# fields='attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time')
#attenderscount = event1['attending_count']
#declinerscount = event1['declined_count']
#interestedcount = event1['interested_count']
#maybecount = event1['maybe_count']
#noreplycount = event1['noreply_count']
print(events)
#print(events['data'])

#attenders = requests.get(“https://graph.facebook.com/v2.7/" + eventid + "/attending?access_token=" + token + "&limit=" + str(attenderscount)) 
#attenders_json = attenders.json()

#admins = requests.get("https://graph.facebook.com/v2.7/" + eventid + "/admins?access_token=" + token)
#admins_json = admins.json()


