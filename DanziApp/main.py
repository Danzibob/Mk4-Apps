"""It's Danzi's app
"""
___license___      = "MIT"
___title___        = "DanziApp"
___dependencies___ = ["app", "database"]
___categories___   = ["emf"]
___bootstrapped___ = False

import http_client, ujson, wifi, time
from tilda import buttons
name = database_get("display-name", "UNKN")
URL = "94.45.255.37:9099"

pin = machine.Pin("PB13", machine.Pin.OUT)
neo = pyb.Neopix(pin)

NUM_BTNS = dir(Buttons)[:10]

params = "name=" + name + "&btn="

def tick():
	for btn in NUM_BTNS:
		if Buttons.is_pressed(btn):
			sendReq(str(btn))

def sendReq(btnNum):
	neo.display(0x888888)
	time.sleep(0.1)
	if (not wifi.nic().is_connected()):
		return False;
	with http_client.post('http://'+URL, urlencoded=params) as resp:
		if resp.text == "OK": neo.display(0x008800)
		else: neo.display(0x880000)

while 1:
	tick()
	time.sleep(0.1)