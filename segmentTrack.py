import analytics
import settings
import events
import string
import random

analytics.write_key = settings.write_key

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def sendEvent():
  eventUserId = str("test-"+id_generator())
  eventName = "adjust-test"
  analytics.track(eventUserId, eventName, events.adjustInstallAttr)
  print("sent " + eventName + " with UID " + eventUserId)

#def on_error(error, items):
#     print("An error occurred:", error)

#sendEvent()