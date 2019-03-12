#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Team: 407AEX
#Contact: t.me/kang_nuubi

from requests import get, post
import json, os
os.system('clear')
print("""
  __ ___ ___    _     _        _ 
 /__  |   |    /  |  / \ |\ | |_ 
 \_| _|_  |    \_ |_ \_/ | \| |_ 
                                 """)
u=input("[!] input username github: ")
print()
re=get('https://api.github.com/users/'+u+'/repos')
a=json.loads(re.text)

items = []
try:
	for item in a:
	    items.append(item['name'])
except TypeError: exit("[!] username tidak ada")

s=len(items)
c=int(1)
while c < s:
	for i in range(len(items)):
		print('\t['+str(c)+"] Install",items[i])
		c+=1
try:
	asu=int(input("\n[?] install yang mana: "))
	os.system('git clone https://github.com/'+u+'/'+items[asu-1])
	print("[!] success installed",items[asu-1])
except (IndexError,ValueError): print("[?] anda waras")
