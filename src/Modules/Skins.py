import re
import time

def skins(wep):
	data = open("assets/Data.txt","r",encoding="utf-8").read()
	i = 0

	qual = "Battle-Scarred"
	value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[0]
	if(len(value)>25):
		qual = "Factory New"

	item_list = searching(wep,qual,i)

	max = len(item_list)
	print("ITEM SKINS : ")
	for i in range(max):
		print((i+1), "\b)" , item_list[i])
		time.sleep(0.0025)
	item = 0

	print("Pick the item skin")
	while (item<1 or item>(len(item_list)+1)):
		try:
			item = int(input("> "))
			if(item<1 or item>(len(item_list)+1)):
				raise ValueError
		except ValueError:
			print("ERROR : INVALID NUMBER")
	item = int(item)-1
	print("\nSelected Skin -", item_list[item])
	return(item_list[item])

def searching(wep,qual,i):
	data = open("assets/Data.txt","r",encoding="utf-8").read()
	item_list = [] 
	while(True):
		try:
			value = re.findall(r": '%s \| (.*?) \(%s\)'" %(wep, qual), data)[i]
			item_list.append(value)
			i = i + 2
		except:
			break
	return item_list