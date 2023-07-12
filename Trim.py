from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
print(drone.get_trim())
drone.set_trim(0, -5)

time.sleep(1)
drone.takeoff()
drone.hover(3)
drone.land()
drone.close()