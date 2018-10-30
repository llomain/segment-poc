import segmentTrack
import time

sleep = time.sleep

def eventSender():
    numberOfEvents = 1
    i = 0
    while i < numberOfEvents: 
        segmentTrack.sendEvent()
        sleep(.5)
        i += 1

eventSender()