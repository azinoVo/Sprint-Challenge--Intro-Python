# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle:
    pass

# 1st gen children
class GroundVehicle(Vehicle):
    pass

class FlightVehicle(Vehicle):
    pass

# Children of Ground and grandchildren of Vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# Children of Flight and grandchildren of Vehicle
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass





