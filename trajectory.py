import numpy

accelDueGrav = 9.80665

def get_vertical(angle, velocity, horizontal):
    """Return vertical position at given horizontal distance for given angle and velocity.
    \nAngle in degrees. Velocity m/s^2. Horizontal metres."""
    angleRadians = numpy.deg2rad(angle)
    vertical = horizontal * numpy.tan(angleRadians) - (accelDueGrav * horizontal ** 2) / (2 * velocity ** 2 * numpy.cos(angleRadians) ** 2)
    return vertical

def get_elevation(velocity, horizontal, vertical, highAngle=False):
    """Return the angle needed to reach point for given velocity
    \nVelocity m/s^2. Horizontal metres. Vertical metres."""
    vertical = 0 - vertical
    if highAngle:
        radians = numpy.tanh( (velocity**2 + numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*horizontal**2 + 2*vertical*velocity**2) )) / (accelDueGrav*horizontal) )
    else:
        radians = numpy.tanh( (velocity**2 - numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*horizontal**2 + 2*vertical*velocity**2) )) / (accelDueGrav*horizontal) )
    angle = numpy.rad2deg(radians)
    return angle

def get_both_angles(velocity, horizontal, vertical):
    """Return a tuple of both angles that can reach the position for given velocity
    \nVelocity m/s^2. Horizontal metres. Vertical metres."""
    angle1 = numpy.rad2deg( numpy.tanh( (velocity**2 + numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*horizontal**2 + 2*vertical*velocity**2) )) / (accelDueGrav*horizontal) ))
    angle2 = numpy.rad2deg( numpy.tanh( (velocity**2 - numpy.sqrt( velocity**4 - accelDueGrav*(accelDueGrav*horizontal**2 + 2*vertical*velocity**2) )) / (accelDueGrav*horizontal) ))
    return angle1, angle2

def time_of_flight(angle, velocity, vertical):
    """Return time of flight in seconds for projectile
    \nAngle degrees. Velocity m/s^2. Vertical metres"""
    a = numpy.deg2rad(angle)
    a = numpy.sin(a)
    return (velocity * a + numpy.sqrt((velocity * a)**2 + 2 * accelDueGrav * vertical)) / accelDueGrav 

def distance_for_time(angle, velocity, time):
    """Return the horizontal distance at given flight time
    \nAngle degrees. Velocity m/s^2. Time seconds."""
    a = numpy.deg2rad(angle)
    a = numpy.cos(a)
    return velocity*a*time

def get_velocity(angle, distance, time):
    """Return the velocity for given angle, distance and time
    \nAngle degrees. distance m. Time seconds."""
    a = numpy.deg2rad(angle)
    a = numpy.cos(a)
    return distance/(a*time)


class Projectile:
    def __init__(self, velocity=None, angle=None, horizontal=None, vertical=None, time=None) -> None:
        self.velocity = velocity
        self.horizontal = horizontal if horizontal else distance_for_time(angle,velocity,time)
        self.vertical = vertical if horizontal else get_vertical(angle,velocity,horizontal)
        self.angle = angle = angle if angle else get_elevation(velocity, horizontal, vertical, highAngle=False)
        self.flightTime = time if time else time_of_flight(angle, velocity, vertical)

    def __repr__(self) -> str:
        return f"""
        #Projectile#
        Initial velocity: {self.velocity} m/s^2
        Horizontal distance: {self.horizontal} m
        Launch height: {self.vertical} m
        Launch angle: {self.angle} degrees
        Flight time: {self.flightTime} s"""


print(Projectile(100,horizontal=500,vertical=-20))
# print(time_of_flight(14.676907516255886,100,0))

print(get_velocity(17.135511651231315,500,5.228749975355362))