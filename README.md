# Projectile Motion

## Description
Module I created to help with a pygame project. Performs various projectile motion calculations.  
Calculations do not take air resistance into account.

Function|Description
--- | ---
`get_initial_height(angle, initialVelocity, horizontalDistance)` | Returns the launch height of the projectile
`get_elevation(initialVelocity, horizontalDistance, initialHeight, highAngle=False)`| Returns the launch angle of projectile. Returns lowest angle unless highAngle set to True
`get_both_angles(initialVelocity, horizontalDistance, initialHeight)`| Returns both possible launch angles as tuple
`time_of_flight(angle, initialVelocity, initialHeight=None)`| Returns time of flight for projectile
`get_distance(angle, initialVelocity, time=None)`| Returns the horizontal distance covered by projectile
`get_initial_velocity(angle, horizontalDistance, time=None)`| Returns the initial velocity of the projectile
