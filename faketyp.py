from pynput.keyboard import Controller
import time
#pynput is a library that gives python access you your keyboard inputs

keyboard = Controller()
#this assigns the Controller() to a variable called keyboard


time.sleep(2)
#this sleep variable would allow me ttime to put the cursor in the desired text field

msg1="Man I hate typing test. Tis is the reason this fella was created. "
#the designated text to be typed


for char in msg1:
	keyboard.press(char)
	keyboard.release(char) 
	#press and release the designated char on the keyboard
	
	time.sleep(0.08)
	#this sleep variable designates the typing speed 