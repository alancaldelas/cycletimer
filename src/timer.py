#! /usr/bin/python3
'''
Alan Caldelas
'''

import time, subprocess,random, webbrowser 
urls = []
def get_videos():
	with open("../db/selection.txt", "r") as f:
		urls = f.readlines()
	print("Complete")
	return urls

def start_timer_rest(completed):
	"""
	Starts a timer based on how many completetions have passed
	"""
	if completed == 5:
		print("You have completed this round rest 25 mins")
		completed = 0
		rtime = 25
	else:
		print("You have completed this section {completed} /5")
		rtime = 5
	print(f"REST TIME HAS BEGUN FOR {rtime}")
	count = 0
	while(count != rtime):
		time.sleep(60)
		count = count + 1
		print(f"Min elapsed... {count} mins")

	subprocess.run(["zenity","--width=250", "--height=250", "--warning", "--text='finished time'"])
	
	print("Rest time has completed")
	
	retrieve_input(completed, urls)
	

def start_timer_read(completed):
	"""
	Starts a study timer of 25 mins and displaying a elapsed time by minutes.
	"""
	print(f"You have completed {completed} so far")
	print("TIME HAS BEGUN")
	count = 0
	while(count != 25):
		time.sleep(60)
		count = count + 1
		print(f"Min elapsed... {count} mins")
	completed = completed + 1
	
	print("Time has completed")
	urls = get_videos()
	webbrowser.open(random.choice(urls))
	subprocess.run(["zenity","--width=250", "--height=250", "--warning", "--text='finished time'"])
	start_timer_rest(completed)

def retrieve_input(completed):
	"""
	Starts the timer, it will be used as sort of the main menu 
	"""
	#TODO: Create more options here, I might want to save profiles of how many I have completed
	user_input = input("Do you wish to begin program?\n>")
	if (str(user_input) == "y"):
		print("Beginning timer for 25 mins")
		start_timer_read(completed)
	else:
		print("Ending program...")
		exit()
def main():
	print("retrieving URLs for YouTube")
	urls = get_videos()
	retrieve_input(0)


main()


