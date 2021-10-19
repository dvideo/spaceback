import uuid
import time

def register_vehicle(vehicle):
  if not vehicle['id']:
    raise RuntimeError('Vehicle must have an ID before being registered!')

  # This could take a while (e.g. pinging an external service)
  time.sleep(3)

  return uuid.uuid4()
