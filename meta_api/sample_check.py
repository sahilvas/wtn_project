from pyfacebook import GraphAPI

#api = GraphAPI(access_token="token")

graph = GraphAPI(app_id='318341643486196', app_secret='2ba2855f0c4e3baab0bf971123477659', application_only_auth=True)
graph.get_authorization_url()
#graph.exchange_user_access_token(response="https://localhost")

#fb.user.get_info(user_id="413140042878187")
print(graph.get_object(object_id="10221877743276286"))
#print(graph.user.get_info(user_id="413140042878187"))
#events = graph.request('/search?q=Poetry&type=event&limit=10000')
#eventList = events['data']
#eventid = eventList[1]['id']
#event1 = graph.get_object(id=eventid,
# fields='attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time')
#attenderscount = event1['attending_count']
#declinerscount = event1['declined_count']
#interestedcount = event1['interested_count']
#maybecount = event1['maybe_count']
#noreplycount = event1['noreply_count']

#print(events)

#attenders = requests.get(“https://graph.facebook.com/v2.7/" + eventid + "/attending?access_token=" + token + "&limit=" + str(attenderscount)) 
#attenders_json = attenders.json()

#admins = requests.get("https://graph.facebook.com/v2.7/" + eventid + "/admins?access_token=" + token)
#admins_json = admins.json()


