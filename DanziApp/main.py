"""It's Danzi's app
"""
___license___      = "MIT"
___title___        = "DanziApp"
___dependencies___ = ["wifi","sleep","http"]
___categories___   = ["emf"]
___bootstrapped___ = False

print("Hello world")

import ugfx, http, sleep#, buttons
#from tilda import Buttons

# Set up graphics
ugfx.clear(ugfx.html_color(0xff0000))

print("Woo graphics")
#Set up URL data
URL = "94.45.255.37:9099"
params = "?btn="

# # set up LEDs
# pin = machine.Pin("PB13", machine.Pin.OUT)
# neo = pyb.Neopix(pin)

# set up buttons
#Buttons.init()
#NUM_BTNS = dir(Buttons)[:10]

ugfx.clear(ugfx.html_color(0xff8800))

def tick():
	ugfx.clear(ugfx.html_color(0x00ff00))
#	for btn in NUM_BTNS:
#		if Buttons.is_pressed(btn):
#			sendReq(str(btn))
	ugfx.clear(ugfx.html_color(0x00ffff))

def sendReq(btnNum):
	ugfx.clear(ugfx.html_color(0x002e5c))
	ugfx.text(1, 10, "You pressed " + str(btnNum), ugfx.WHITE)
	#neo.display(0x888888)
	time.sleep(0.2)
	with http.get('http://'+URL, urlencoded=params+str(btnNum)) as resp:
		if resp.text == "OK": 
			#neo.display(0x008800)
			ugfx.text(1, 30, "Sent OK", ugfx.WHITE)
		else: 
			#neo.display(0x880000)
			ugfx.text(1, 30, "Bad Response:" + resp.text, ugfx.WHITE)

ugfx.clear(ugfx.html_color(0xffff00))

try:
	while 1:
		tick()
except e:
	ugfx.clear(ugfx.html_color(0x002e5c))
	ugfx.text(1, 10, str(e), ugfx.WHITE)
	