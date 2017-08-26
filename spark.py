from ciscosparkapi import CiscoSparkAPI
import config 

api = CiscoSparkAPI(config.API_KEY)

def list_rooms(keyword):
	all_rooms = api.rooms.list() 
	demo_rooms = [room for room in all_rooms if keyword in room.title]
	return demo_rooms