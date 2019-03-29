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

class GroundVehicle(Vehicle):
    pass

x = GroundVehicle("Car")
y = GroundVehicle("Motorcycle")

print(x)
print(y)

class FlightVehicle(Vehicle):
    pass

z = FlightVehicle("Airplane")

print(z)


class Starship(Vehicle):
    pass
