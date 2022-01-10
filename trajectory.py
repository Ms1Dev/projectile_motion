import numpy
import timeit

accelDueGrav = 9.80665

def get_vertical(angle, velocity, distance):
    """Return vertical position at given distance for given angle and velocity.
    \nAngle in degrees. Velocity m/s^2. Distance metres."""
    angleRadians = numpy.deg2rad(angle)
    vertical = distance * numpy.tan(angleRadians) - (accelDueGrav * distance ** 2) / (2 * velocity ** 2 * numpy.cos(angleRadians) ** 2)
    return vertical

def get_elevation(velocity, distance, vertical, highAngle=False):
    """Return the angle needed to reach point for given velocity
    \nVelocity m/s^2. Distance metres. Vertical metres."""
    if highAngle:
        radians = numpy.tanh( (velocity**2 + numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*distance**2 + 2*vertical*velocity**2) )) / (accelDueGrav*distance) )
    else:
        radians = numpy.tanh( (velocity**2 - numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*distance**2 + 2*vertical*velocity**2) )) / (accelDueGrav*distance) )
    angle = numpy.rad2deg(radians)
    return angle

def time_of_flight(angle, velocity, vertical):
    """Return time of flight in seconds for projectile
    \nAngle degrees. Velocity m/s^2. Vertical metres"""
    a = numpy.deg2rad(angle)
    a = numpy.sin(a)
    return (velocity * a + numpy.sqrt((velocity * a)**2 + 2 * accelDueGrav * vertical)) / accelDueGrav 

 

# print(timeit.timeit('time_of_flight(1.0119579943588308, 800, 10)', setup="from __main__ import time_of_flight"))


