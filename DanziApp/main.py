"""It's Danzi's app
"""
___license___      = "MIT"
___title___        = "DanziApp"
___dependencies___ = ["app", "database", "http_client", "wifi","ugfx"]
___categories___   = ["emf"]
___bootstrapped___ = False

import http_client, wifi, time, ugfx
from tilda import buttons

# Set up URL data
name = database_get("display-name", "UNKN")
URL = "94.45.255.37:9099"
params = "name=" + name + "&btn="

# set up LEDs
pin = machine.Pin("PB13", machine.Pin.OUT)
neo = pyb.Neopix(pin)

# set up buttons
buttons.init()
NUM_BTNS = dir(Buttons)[:10]

# Set up graphics
ugfx_helper.init()

def tick():
	for btn in NUM_BTNS:
		if Buttons.is_pressed(btn):
			sendReq(str(btn))

def sendReq(btnNum):
	ugfx.clear(ugfx.html_color(0x002e5c))
	ugfx.text(1, 10, "You pressed " + str(btnNum), ugfx.WHITE)
	neo.display(0x888888)
	time.sleep(0.2)
	if (not wifi.nic().is_connected()):
		return False;
	with http_client.post('http://'+URL, urlencoded=params+str(btnNum)) as resp:
		if resp.text == "OK": 
			neo.display(0x008800)
			ugfx.text(1, 30, "Sent OK", ugfx.WHITE)
		else: 
			neo.display(0x880000)
			ugfx.text(1, 30, "Bad Response:" + resp.text, ugfx.WHITE)
		time.sleep(1)

while 1:
	tick()
	time.sleep(0.1)
	ugfx.clear(ugfx.html_color(0x002e5c))