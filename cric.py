
#Firstly install these two packages i.e. sports.py and py-notifier

#pip install sports.py
#pip install py-notifier
import time
import sports
from pynotifier import Notification
while(True):
    MatchInfo=sports.get_sport("Cricket")
    Notification(title="Live Cricket Score", description=str(MatchInfo),duration=10,icon_path='C:\\Users\\H P\\Downloads\\CricbuzzIcon.ico').send()
    time.sleep(10)
