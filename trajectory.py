import numpy

accelDueGrav = 9.80665

def get_initial_height(angle, initialVelocity, horizontalDistance):
    """Return initial height needed to reach horizontal distance for given angle and initial velocity.
    \nAngle in degrees. Initial velocity m/s. Horizontal metres."""
    angleRadians = numpy.deg2rad(angle)
    initialHeight = horizontalDistance * numpy.tan(angleRadians) - (accelDueGrav * horizontalDistance ** 2) / (2 * initialVelocity ** 2 * numpy.cos(angleRadians) ** 2)
    initialHeight = 0 - initialHeight
    return initialHeight

def get_elevation(initialVelocity, horizontalDistance, initialHeight, highAngle=False):
    """Return the angle needed to reach point for given initial velocity
    \nInitial velocity m/s. Horizontal metres. initialHeight metres."""
    initialHeight = 0 - initialHeight
    if highAngle:
        radians = numpy.tanh( (initialVelocity**2 + numpy.sqrt( initialVelocity**4 - accelDueGrav*(accelDueGrav*horizontalDistance**2 + 2*initialHeight*initialVelocity**2) )) / (accelDueGrav*horizontalDistance) )
    else:
        radians = numpy.tanh( (initialVelocity**2 - numpy.sqrt( initialVelocity**4 - accelDueGrav*(accelDueGrav*horizontalDistance**2 + 2*initialHeight*initialVelocity**2) )) / (accelDueGrav*horizontalDistance) )
    angle = numpy.rad2deg(radians)
    return angle

def get_both_angles(initialVelocity, horizontalDistance, initialHeight):
    """Return tuple of both angles needed to reach point for given initial velocity
    \nInitial velocity m/s. Horizontal metres. initialHeight metres."""
    initialHeight = 0 - initialHeight
    angle1 = numpy.rad2deg( numpy.tanh( (initialVelocity**2 + numpy.sqrt( initialVelocity**4 - accelDueGrav*(accelDueGrav*horizontalDistance**2 + 2*initialHeight*initialVelocity**2) )) / (accelDueGrav*horizontalDistance) ))
    angle2 = numpy.rad2deg( numpy.tanh( (initialVelocity**2 - numpy.sqrt( initialVelocity**4 - accelDueGrav*(accelDueGrav*horizontalDistance**2 + 2*initialHeight*initialVelocity**2) )) / (accelDueGrav*horizontalDistance) ))
    return angle1, angle2

def time_of_flight(angle, initialVelocity, initialHeight=None):
    """Return time of flight in seconds for projectile. If initial height is not given then maximum flight time is returned for target that is the same height as initial height.
    \nAngle degrees. Initial velocity m/s. initial height metres"""
    angle = numpy.deg2rad(angle)
    angle = numpy.sin(angle)
    if initialHeight:
        time = (initialVelocity * angle + numpy.sqrt((initialVelocity * angle)**2 + 2 * accelDueGrav * initialHeight)) / accelDueGrav 
    else:
        time = (2*initialVelocity*angle)/accelDueGrav
    return time

def get_distance(angle, initialVelocity, time=None):
    """Return the horizontal distance for initial velocity and angle. If no time argument is given then maximum distance is returned for target that is the same height as initial height.
    \nAngle degrees. Initial velocity m/s. Time seconds."""
    if time:
        angle = numpy.deg2rad(angle)
        angle = numpy.cos(angle)
        distance = initialVelocity*angle*time
    else:
        angle = numpy.deg2rad(angle)
        angle = numpy.sin((2*angle))
        distance = (initialVelocity**2*angle)/accelDueGrav
    return distance

def get_initial_velocity(angle, horizontalDistance, time=None):
    """Return the initial velocity for given angle, distance and time. If no time argument is given then initial velocity is returned for target that is the same height as initial height.
    \nAngle degrees. Distance m. Time seconds."""
    angle = numpy.deg2rad(angle)
    if time:
        velocity = horizontalDistance/(numpy.cos(angle)*time)
    else:
        velocity = numpy.sqrt(horizontalDistance*accelDueGrav/numpy.sin(angle*2))
    return velocity 

