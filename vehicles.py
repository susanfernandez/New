class Vehicles:
    """Class for describing vehicles"""

    def __init__(self, name):
        self.namevar = name
        self.wheels = 0
        self.doors = 0
        self.seats = 0
        self.passengers = []

    def num_wheels(self, wheels):
        self.wheels = wheels
        print(self.wheels, "wheels")

    def num_doors(self, doors):
        self.doors = doors
        print(self.doors, "doors")

    def num_seats(self, seats):
        self.seats = seats
        print(self.seats, "seats")

    def num_pass(self, passengers):
        self.passengers = passengers
        print(v1.passengers, "---> Passengers")

#otherwayforpasslist
    def add_pass(self, passengers):
        self.passengers1.append(passengers)

v1 = Vehicles("Car") #creates a new vehicles outside of the class
#pass in "type" or "model" in this init function

print(v1.namevar)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#car info
v1.num_wheels(4)
v1.num_doors(2)
v1.num_seats(4)

#otherwayforpasslist
v1.add_pass("Johnny")
print(v1.passengers1)

#passenger list info
listpass= ["Johnny", "Bob", "Mary"]
v1.num_pass(listpass)
