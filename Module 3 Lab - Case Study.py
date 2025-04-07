""" 
This code will use different class types, attributes, and inheritence. 
It will create an app that will accept user input on car information such as
year, make, model, number of doors, and roof type then output the infomation.
"""




class Vehicle:                                          # Super class that contains an attribute for vehicle type.
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):                              # Class that inherits super class attributes and it's own attributes.
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')                         # Initializes the super class.
        self.year = year
        self.make = make 
        self.model = model 
        self.doors = doors
        self.roof = roof  
    def vehicle_data(self):                             # Easy-to-read output of formatted user data.
        print(f'Vehicle type: {self.vehicle_type}')
        print(f'Year: {self.year}')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'# of doors: {self.doors}')
        print(f'Roof type: {self.roof}')

def main():                                             # App that accepts user input for the car and stores info in the attributes.
    print("This is the car app, enter your car's information!")

    year = input('Enter the year: ')
    make = input('Enter the make: ')
    model = input('Enter the model: ')
    doors = input('Enter the # of doors (2 or 4): ')
    roof = input('Enter the roof type (solid or sun roof): ')

    car = Automobile(year, make, model, doors, roof)    # Instance of the Automobile class.

    car.vehicle_data()                                  # Displays the user car information.

if __name__ == "__main__":                              # Calls the main function to start the app. 
    main()



    


