import pyautogui
import os

a=int(input('1'))
b=int(input('2'))
c=int(input('3'))
d=0



while True:
	e=input()
	if len(e)==0:
		try:
			os.makedirs(f"D:/backup C/skripty/ODRABIAMY SCRAPER XD/{a}/{b}/{c}")
		except:
			pass
		pyautogui.screenshot(f"./{a}/{b}/{c}/{d}.png", region=(400, 125, 780, 915))
		d+=1
	elif len(e)==1:
		d=0
		c+=1
	elif len(e)==2:
		d=0
		c=1
		b+=1
	elif len(e)==3:
		d=0
		c=1
		b=1
		a+=1
	




pyautogui.screenshot(f"./{a}/{c}/{c}/{d}.png", region=(400, 125, 780, 915))