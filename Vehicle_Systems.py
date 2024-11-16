class Vehicle:
    def __init__(self, t, c, n, b):
        self.__type=t
        self.__color=c
        self.__num_wheels=n
        self.__brand=b

    def display(self):
        print("Type: "+self.__type)
        print("Color: "+self.__color)
        print("Number of wheels: "+self.__num_wheels)
        print("Brand: "+self.__brand)

    def modify(self):
        while 1:
            print("1. Color")
            print("2. Exit")
            choice=int(input("Choose from the menu what you want"))
            if choice==1:
                color=input("Type the new color of the Vehicle: ")
            elif choice==2:
                break
            else:
                print("Invalid input. Try again.")

class Truck(Vehicle):
    def __init__(self, t, c, n, b, ax, no_ax, bod_len, w):
        Vehicle.__init__(self,t,c,n,b)
        self.__axle_ratio=ax
        self.__no_axles =no_ax
        self.__body_length = bod_len
        self.__weight =w

    def display(self):
        Vehicle.display(self)
        print("Axle Ratio: "+self.__axle_ratio)
        print("Number of axles: "+self.__no_axles)
        print("Body Length: "+self.__body_length)
        print("Weight: "+self.__weight)

    def modify(self):
        Vehicle.modify(self)
        while 1:
            print("1. Axle Ratio")
            print("2. Number of axles")
            print("3. Weight")
            print("4. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__axle_ratio = input("Type new axle ratio: ")
            elif choice == 2:
                self.__no_axles = input("Type the new number of axles: ")
            elif choice==3:
                self.__weight=input("Type the new weight: ")
            elif choice==4:
                break
            else:
                print("invalid input. Try Again.")

class Car(Vehicle):
    def __init__(self, t, c, n, b,h, mpg, m, y):
        Vehicle.__init__(self,t,c,n,b)
        self.__horsepower=h
        self.__miles_per_gallon=mpg
        self.__model=m
        self.__year=y

    def display(self):
        Vehicle.display(self)
        print("Horse Power: "+self.__horsepower)
        print("Miles per gallon: "+self.__miles_per_gallon)
        print("Model: "+self.__model)
        print("Year: "+self.__year)

    def modify(self):
        Vehicle.modify(self)
        while 1:
            print("1. horse power")
            print("2. Miles per gallon")
            print("3. Exit")
            choice=int(input("Choose a number from the menu for what you want to modify: "))
            if choice==1:
                self.__horsepower=input("Type new horse power: ")
            elif choice==2:
                self.__miles_per_gallon = input("Type miles per gallon: ")
            elif choice==3:
                break
            else:
                print("invalid input. Try Again.")

class Motorbike(Vehicle):
    def __init__(self,t,c,n,b,ec,ft,st):
        Vehicle.__init__(self,t,c,n,b)
        self.__engine_capacity=ec
        self.__fuel_type=ft
        self.__seat_height=st

    def display(self):
        Vehicle.display(self)
        print("Engine Capacity: "+self.__engine_capacity)
        print("Fuel Type: "+self.__fuel_type)
        print("Seat Height: "+self.__seat_height)

    def modify(self):
        Vehicle.modify(self)
        while 1:
            print("1. Color")
            print("2. Exit")
            choice = int(input("Choose from the menu what you want"))
            if choice==1:
                self.__seat_height=input("Type the new seat height: ")
            elif choice==2:
                break


class TowTruck(Truck):
    def __init__(self,t,c,n,b,ax,no_axle,bod_len,w,mtc,dt,bt):
        Truck.__init__(self,t,c,n,b,ax,no_axle,bod_len,w)
        self.__max_tow_cap=mtc
        self.__drive_type=dt
        self.__bed_type=bt

    def display(self):
        Truck.display(self)
        print("Maximum towing capacity: "+self.__max_tow_cap)
        print("Type of drive train: "+self.__drive_type)
        print("Type of tow bed: "+self.__bed_type)

    def modify(self):
        Truck.modify(self)
        while 1:
            print("1. Maximum towing capacity")
            print("2. Type of tow bed")
            print("3. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__max_tow_cap = input("Type new horse power: ")
            elif choice == 2:
                self.__bed_type = input("Type miles per gallon: ")
            elif choice == 3:
                break
            else:
                print("invalid input. Try Again.")


class Tanker(Truck):
    def __init__(self,t,c,n,b,ax,no_axle,bod_len,w,vt,tm,i):
        Truck.__init__(self,t,c,n,b,ax,no_axle,bod_len,w)
        self.__valve_type=vt
        self.__tank_material=tm
        self.__insulated=i

    def display(self):
        Truck.display(self)
        print("Valve type: "+self.__valve_type)
        print("Tank Material: "+self.__tank_material)
        print("Is insulated: "+self.__valve_type)

    def modify(self):
        Truck.modify(self)
        while 1:
            print("1. Valve type")
            print("2. Tank Material")
            print("3. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__valve_type = input("Type new valve type: ")
            elif choice == 2:
                self.__tank_material = input("Type the new tank material: ")
            elif choice == 3:
                break
            else:
                print("invalid input. Try Again.")

class Tractor_Trailer(Truck):
    def __init__(self, t, c, n, b, ax, no_axle, bod_len, w, gcw, fc, mpc):
        Truck.__init__(self, t, c, n, b, ax, no_axle, bod_len, w)
        self.__gross_combo_w = gcw
        self.__fuel_cap = fc
        self.__max_pay_cap = mpc

    def display(self):
        Truck.display(self)
        print("Gross combination weight: "+self.__gross_combo_w)
        print("Fuel Capacity: "+self.__fuel_cap)
        print("Maximum payload capacity: "+self.__max_pay_cap)

    def modify(self):
        Truck.modify(self)
        while 1:
            print("1. Gross combination weight")
            print("2. Exit")
            choice=int(input("Choose from the menu what you want"))
            if choice==1:
                color=input("Enter the new gross combination weight of the Vehicle: ")
            elif choice==2:
                break
            else:
                print("Invalid input. Try again.")

class Sedan(Car):
    def __init__(self,t,c,n,b,h,mpg,m,y,st,ts,fe):
        Car.__init__(self,t,c,n,b,h,mpg,m,y)
        self.__sedan_type=st
        self.__trunk_style=ts
        self.__fuel_efficiency=fe

    def display(self):
        Car.display(self)
        print("Sedan type: "+self.__sedan_type)
        print("Trunk style: "+self.__trunk_style)
        print("Fuel efficiency: "+self.__fuel_efficiency)

    def modify(self):
        Car.modify(self)
        while 1:
            print("1. Fuel Efficiency")
            print("2. Trunk Style")
            print("3. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__fuel_efficiency = input("Type new fuel efficiency: ")
            elif choice == 2:
                self.__trunk_style = input("Type the new trunk style: ")
            elif choice == 3:
                break
            else:
                print("invalid input. Try Again.")


class SUV(Car):
    def __init__(self, t, c, n, b, h, mpg, m, y, awd, st, rr):
        Car.__init__(self, t, c, n, b, h,mpg,m,y)
        self.__all_wheel_drive = awd
        self.__suspension_type = st
        self.__roof_rack = rr

    def display(self):
        Car.display(self)
        print("All Wheel Drive: "+self.__all_wheel_drive)
        print("Suspension type: "+self.__suspension_type)
        print("Has a roof rack: "+self.__roof_rack)

    def modify(self):
        Car.display(self)
        while 1:
            print("1. All wheel drive")
            print("2. Suspension type")
            print("3. Roof rack")
            print("4. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__all_wheel_drive = input("Type whether it has an all wheel drive: ")
            elif choice == 2:
                self.__suspension_type = input("Type the new suspension type ")
            elif choice == 3:
                self.__roof_rack = input("Type whether it has a roof rack: ")
            elif choice == 4:
                break
            else:
                print("invalid input. Try Again.")

class Coupe(Car):
    def __init__(self, t, c, n, b, h, mpg, m, y, td, tor, a):
        Car.__init__(self, t, c, n, b, h, mpg, m, y)
        self.__has_two_door = td
        self.__torque = tor
        self.__acceleration = a

    def display(self):
        Car.display(self)
        print("Has two doors: "+self.__has_two_door)
        print("torque: "+self.__torque)
        print("acceleration: "+self.__acceleration)

    def modify(self):
        while 1:
            print("1. Torque")
            print("2. Acceleration")
            print("3. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__torque = input("Type new torque: ")
            elif choice == 2:
                self.__acceleration = input("Type the new acceleration: ")
            elif choice == 3:
                break
            else:
                print("invalid input. Try Again.")

class Enduro(Motorbike):
    def __init__(self,t,c,n,b,ec,ft,st,susTrav,es,gt):
        Motorbike.__init__(t,c,n,b,ec,ft,st)
        self.__Suspension_travel = susTrav
        self.__electric_Start = es
        self.__gearbox_type = gt

    def display(self):
        Motorbike.display(self)
        print("Travel distance of the suspension: "+self.__Suspension_travel)
        print("Has electric start: " + self.__electric_Start)
        print("gearbox type: " + self.__gearbox_type)

    def modify(self):
        Motorbike.modify(self)
        while 1:
            print("1. Travel distance of suspension")
            print("2. Gearbox type")
            print("3. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__Suspension_travel = input("Type new travel distance of suspension: ")
            elif choice == 2:
                self.__gearbox_type = input("Type the new gearbox type: ")
            elif choice == 3:
                break
            else:
                print("invalid input. Try Again.")

class Chopper(Motorbike):
    def __init__(self,t,c,n,b,ec,ft,st,hb,fl,ra):
        Motorbike.__init__(self,t,c,n,b,ec,ft,st)
        self.__handle_bar=hb
        self.__fork_length=fl
        self.__rake_angle=ra

    def display(self):
        Motorbike.display(self)
        print("Type of handle bars: "+self.__handle_bar)
        print("Type the fork length: "+self.__fork_length)
        print("Type the rake angle: "+self.__rake_angle)

    def modify(self):
        Motorbike.display(self)
        while 1:
            print("1. Type of handle bars")
            print("2. Type the fork length")
            print("3. Type the rake angle")
            print("4. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__handle_bar = input("Type new type of handle bars: ")
            elif choice == 2:
                self.__fork_length = input("Type the new fork length: ")
            elif choice == 3:
                self.__rake_angle = input("Type the new rake angle: ")
            elif choice == 4:
                break
            else:
                print("invalid input. Try Again.")

class Cross(Motorbike):
    def __init__(self,t,c,n,b,ec,ft,st,tt,et,gr):
        Motorbike.__init__(self,t, c, n, b, ec, ft, st)
        self.__tyre_type=tt
        self.__exhaust_type=et
        self.__gear_ratio=gr

    def display(self):
        Motorbike.display(self)
        print("Tyre type: "+self.__tyre_type)
        print("Exhaust type: "+self.__exhaust_type)
        print("Gear Ratio: "+self.__gear_ratio)

    def modify(self):
        Motorbike.modify(self)
        while 1:
            print("1. Tyre type")
            print("2. Exhaust type")
            print("3. Gear Ratio")
            print("4. Exit")
            choice = int(input("Choose a number from the menu for what you want to modify: "))
            if choice == 1:
                self.__tyre_type = input("Type new tyre type: ")
            elif choice == 2:
                self.__exhaust_type = input("Type the new exhaust: ")
            elif choice == 3:
                self.__gear_ratio = input("Type the new gear ratio: ")
            elif choice == 4:
                break
            else:
                print("invalid input. Try Again.")















