# TwitterDateBot
This bot is currently running on Twitter as: @Pi_Date_Bot  
_Originally coded by "TheGuruGamer" /u/123icebuggy @123icebuggy_  

# How To Use on a RaspberryPi?
To install this, first run `pip install tweepy` in the terminal.

Download the files from this repository and put them into a folder that you can easily `cd` to.   
The next command after you have cd'd to the folder is 
```
python3 setup.py
```
Run through the setup process and a new file called `auth.py` will be created. This is so the script can tweet on your account.
Next, to run the bot use:
```
python3 bot.py
```
The bot should now post at 6AM every day; as long there is a constant terminal process and internet connection.
**WARNING:** The bot will stop if you close the terminal, so I reccomend using something like tmux.

## Changelog
v1.0.1: Initial Release; with comments  
v1.0.0: _Original Version._  
