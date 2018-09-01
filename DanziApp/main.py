"""It's Danzi's app
"""
___license___      = "MIT"
___title___        = "DanziApp"
___dependencies___ = ["app", "database"]
___categories___   = ["emf"]
___bootstrapped___ = False

import http_client, ujson, wifi
from tilda import buttons
name = database_get("display-name", "UNKN")
URL = "94.45.255.37:9099"

NUM_BTNS = dir(Buttons)[:10]

params = "name=" + name + "&btn="

def tick():
	for btn in NUM_BTNS:
		if Buttons.is_pressed(btn):
			sendReq(str(btn))

def sendReq(btnNum):
	if (not wifi.nic().is_connected()):
		return False;
	with http_client.post('http://'+URL, urlencoded=params) as resp:
		if resp.text == "OK": print("woo")
		else: print("wat")
