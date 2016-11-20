import auth #this imports the auth.py file which in in the same directory
import time #this module is used for... I'm not sure, I don't think this is meant to be here
from datetime import datetime #Ah here it is, I used from to select the module, and the import to import a certain function form that module
from time import sleep #Again using from and import, this module is used to pause a script
ok = True #Just a variable I set to true in order to set up the loop
t = auth.login() #In order to login into Twitter. I use auth.login() because in the auth.py file, there is a function called login, which returns a function called api, but I have called it t
while True: #Infinite loop
	time = str(datetime.now()) #Current time
	time = time[:-10].replace(':', '')#Shortens the time and replaces ':' with ''
	time = time[11:] #Shortening it futher, essentially making it military time
	if time == '0600': #If the time is 6 AM
		year = str(datetime.now())[:-22] #Getting the year but taking 22 characters of the end of the string
		month = str(datetime.now())[5:-19] #Gets the month by taking 5 characters off the start of the string, and 19 off the end
		day = str(datetime.now())[8:-16] #Gets the time by taking 8 characters off the start of string, and 16 off the end
	
		tweet = 'The Date Today Is: %s/%s/%s.' % (day, month, year) #Here I use %s, which is a filler for a string. At the end I use % (day, month, year) Replacing the %s's with the day, month, and year in that order.
		if ok == True: #Checking if the  variable defined on line 5 is still set to True
			t.update_status(tweet) #Posts the tweet, using t. On line 6 we define t
			ok = False #Setting ok to False, meaning the tweet will not be posted again, as on line 17, we say that we only get to this part if ok is set to True
	if time == '0601':#1 mintue after posting the tweet
		ok = True #Set Ok to true, so that on the next day as 0600, ok will be True, meaning that the tweet will be allowed to be posted again
	sleep(30) #Sleep for 30 seconds