import pyautogui
from pynput import keyboard
import os

a=int(input('1'))
b=int(input('2'))
c=int(input('3'))
d=0


def on_press(key):
	global a, b, c, d
	if str(key) == "Key.space":
		try:
			os.makedirs(f"D:/backup C/skripty/ODRABIAMY SCRAPER XD/{a}/{b}/{c}")
		except:
			pass
		pyautogui.screenshot(f"./{a}/{b}/{c}/{d}.png", region=(400, 125, 780, 915))
		d+=1
	elif str(key) == "'1'":
		d=0
		c+=1
	elif str(key) == "'2'":
		d=0
		c=1
		b+=1
	elif str(key) == "'3'":
		d=0
		c=1
		b=1
		a+=1
	print(f"{a}/{b}/{c}/{d}")
	

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

