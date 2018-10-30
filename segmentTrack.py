import analytics
import settings
import events
import string
import random

analytics.write_key = settings.write_key

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def sendEvent():
  analytics.track("test-"+id_generator(), 'adjust-test', events.adjustInstallAttr)

def on_error(error, items):
     print("An error occurred:", error)

#sendEvent()