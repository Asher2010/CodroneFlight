from codrone_edu.drone import *

drone = Drone()
drone.pair()
print("Paired!")
drone.takeoff()
print("In the air!")
print("Landing")
drone.emergency_stop()
drone.close()
