from xml.sax.saxutils import escape

import Vehicle_Systems
vs=Vehicle_Systems

tows=[]
tankers=[]
tracts=[]

sedans=[]
suvs=[]
coupes=[]

enduros=[]
choppers=[]
crosses=[]

def add_truck():
    while 1:
        print("1. Add a Tow Truck")
        print("2. Display Tow Trucks")
        print("3. Modify Tow Trucks")
        print("4. Add a Tanker")
        print("5. Display a Tanker")
        print("6. Modify a Tanker")
        print("7. Add a Tractor Trailer")
        print("8. Display a Tractor Trailer")
        print("9. Modify a Tractor Trailer")
        print("99. Exit menu")
        choice = int(input("Please choose a number from the menu what you want to do: "))

        if choice==99:
            break

        elif choice==1:
            t=input("Enter the type: ")
            c=input("Enter the color: ")
            n=input("Enter the number of wheels: ")
            b=input("Enter the brand: ")
            ax=input("Enter the axle ratio: ")
            no_ax=input("Enter the number of axles: ")
            bod_len=input("Enter the body length: ")
            w=input("Enter the weight: ")
            mtc=input("Enter maximum tow capacity: ")
            dt=input("Enter drive type: ")
            bt=input("Enter the bed type: ")
            tow=vs.TowTruck(t,c,n,b,ax,no_ax,bod_len,w,mtc,dt,bt)
            tows.append(tow)

        elif choice==2:
            if len(tows)>0:
                for i in range(0, len(tows)):
                    print(f"-- Tow Truck {i + 1} --")
                    tows[i].display()
                    print(" ")
            else:
                print("No Tow Trucks currently.")

        elif choice==3:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(tows):
                for i in range(0, len(tows)):
                    tows[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==4:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            ax = input("Enter the axle ratio: ")
            no_ax = input("Enter the number of axles: ")
            bod_len = input("Enter the body length")
            w = input("Enter the weight: ")
            vt=input("Valve type: ")
            tm=input("Tank Material: ")
            i=input("Type whether it's insulated or not (yes or no): ")
            tank=vs.Tanker(t, c, n, b, ax, no_ax, bod_len, w, vt, tm, i)
            tankers.append(tank)

        elif choice==5:
            if len(tankers)>0:
                for i in range(0, len(tankers)):
                    print(f"-- Tanker {i + 1} --")
                    tankers[i].display()
                    print(" ")
            else:
                print("No tankers currently.")

        elif choice==6:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(tankers):
                for i in range(0, len(tankers)):
                    tankers[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==7:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            ax = input("Enter the axle ratio: ")
            no_ax = input("Enter the number of axles: ")
            bod_len = input("Enter the body length")
            w = input("Enter the weight: ")
            gcw = input("Gross combination weight: ")
            fc = input("Fuel Capacity: ")
            mpc = input("Maximum payload capacity: ")
            tractor= vs.Tractor_Trailer(t, c, n, b, ax, no_ax, bod_len, w, gcw, fc, mpc)
            tracts.append(tractor)

        elif choice==8:
            if len(tracts)>0:
                for i in range(0, len(tracts)):
                    print(f"-- Tractor Trailer {i + 1} --")
                    tracts[i].display()
                    print(" ")
            else:
                print("No Tractor Trailers currently.")

        elif choice==9:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(tracts):
                for i in range(0, len(tracts)):
                    tracts[pick-1].modify()
            else:
                print("No cross found.")
        else:
            print("Invalid input. Try again.")

def add_car():
    while 1:
        print("1. Add a Sedan")
        print("2. Display a Sedan")
        print("3. Modify a Sedan")
        print("4. Add a SUV")
        print("5. Display a SUV")
        print("6. Modify a SUV")
        print("7. Add a Coupe")
        print("8. Display a Coupe")
        print("9. Modify a Coupe")
        print("99. Exit menu")
        choice = int(input("Please choose a number from the menu what you want to do: "))

        if choice==99:
            break

        elif choice==1:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            h = input("Enter the horse power ")
            mpg =input("Enter the miles per gallon: ")
            m = input("Enter the model: ")
            y = input("Enter the year: ")
            st = input("Enter the Sedan type: ")
            ts= input("Enter the trunk style: ")
            fe=input("Enter the fuel efficiency: ")
            sedan = vs.Sedan(t,c,n,b,h,mpg,m,y,st,ts,fe)
            sedans.append(sedan)

        elif choice==2:
            if len(sedans)>0:
                for i in range(0, len(sedans)):
                    print(f"-- Sedan {i + 1} --")
                    sedans[i].display()
                    print(" ")
            else:
                print("No sedans currently.")

        elif choice==3:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(sedans):
                for i in range(0, len(sedans)):
                    sedans[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==4:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            h = input("Enter the horse power ")
            mpg = input("Enter the miles per gallon: ")
            m = input("Enter the model: ")
            y = input("Enter the year: ")
            awd = input("Enter whether it's all wheel drive or not (yes or no): ")
            st = input("Enter the suspension type: ")
            rr = input("Enter whether it has a roof rack or not: ")
            suv = vs.SUV(t, c, n, b, h, mpg, m, y, awd, st, rr)
            suvs.append(suv)

        elif choice==5:
            if len(suvs)>0:
                for i in range(0, len(suvs)):
                    print(f"-- SUV {i + 1} --")
                    suvs[i].display()
                    print(" ")
            else:
                print("No SUVs currently.")

        elif choice==6:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(suvs):
                for i in range(0, len(suvs)):
                    suvs[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==7:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            h = input("Enter the horse power ")
            mpg = input("Enter the miles per gallon: ")
            m = input("Enter the model: ")
            y = input("Enter the year: ")
            td = input("Enter whether it has two doors or not (yes no): ")
            tor = input("Enter the torque: ")
            a = input("Enter acceleration: ")
            coupe = vs.Coupe(t, c, n, b, h, mpg, m, y, td, tor, a)
            coupes.append(coupe)

        elif choice==8:
            if len(coupes)>0:
                for i in range(0, len(coupes)):
                    print(f"-- Coupe {i + 1} --")
                    coupes[i].display()
                    print(" ")
            else:
                print("No Coupes currently")

        elif choice==9:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(coupes):
                for i in range(0, len(coupes)):
                    coupes[pick-1].modify()
            else:
                print("No cross found.")

        else:
            print("Invalid input. Try again.")

def add_motorbike():
    while 1:
        print("1. Add an Enduro")
        print("2. Display an Enduro")
        print("3. Modify an Enduro")
        print("4. Add a Chopper")
        print("5. Display a Chopper")
        print("6. Modify a Chopper")
        print("7. Add a Cross")
        print("8. Display a Cross")
        print("9. Modify a Cross")
        print("99. Exit menu")

        choice=int(input("Please choose a number from the menu for what you like to do: "))
        if choice==99:
            break

        elif choice==1:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            ec =input("Enter the engine capacity: ")
            ft =input("Enter the fuel type: ")
            st =input("Enter the seat height: ")
            susTrav= input("Enter the travel distance of the suspension: ")
            es=input("Enter whether it has an electric start or not (yes or no) ")
            gt=input("Enter the gearbox type: ")
            enduro=vs.Enduro(t,c,n,b,ec,ft,st,susTrav,es,gt)
            enduros.append(enduro)

        elif choice==2:
            if len(enduros)>0:
                for i in range(0, len(enduros)):
                    print(f"-- Enduro {i + 1} --")
                    enduros[i].display()
                    print(" ")
            else:
                print("No Enduros currently")

        elif choice==3:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(enduros):
                for i in range(0, len(enduros)):
                        enduros[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==4:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            ec = input("Enter the engine capacity: ")
            ft = input("Enter the fuel type: ")
            st = input("Enter the seat height: ")
            hb = input("Enter the type of handle bar: ")
            fl = input("Enter the fork length ")
            ra = input("Enter the rake angle: ")
            chop = vs.Chopper(t, c, n, b, ec, ft, st, hb, fl, ra)
            choppers.append(chop)

        elif choice==5:
            if len(choppers)>0:
                for i in range(0, len(choppers)):
                    print(f"-- Chopper {i + 1} --")
                    choppers[i].display()
                    print(" ")
            else:
                print("No choppers currently.")

        elif choice==6:
            pick = int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(choppers):
                for i in range(0, len(choppers)):
                    choppers[pick-1].modify()
            else:
                print("No cross found.")

        elif choice==7:
            t = input("Enter the type: ")
            c = input("Enter the color: ")
            n = input("Enter the number of wheels: ")
            b = input("Enter the brand: ")
            ec = input("Enter the engine capacity: ")
            ft = input("Enter the fuel type: ")
            st = input("Enter the seat height: ")
            tt = input("Enter the tyre type: ")
            et = input("Enter the exhaust type ")
            gr = input("Enter the gear ratio: ")
            cross=vs.Cross(t,c,n,b,ec,ft,st,tt,et,gr)
            crosses.append(cross)

        elif choice==8:
            if len(crosses)>0:
                for i in range(0, len(crosses)):
                    print(f"-- Cross {i + 1} --")
                    crosses[i].display()
                    print(" ")
            else:
                print("No crosses currently.")

        elif choice==9:
            pick=int(input("Choose a number from the inventory of what you want to modify: "))
            if 0 < pick <= len(crosses):
                for i in range(0,len(crosses)):
                    crosses[pick-1].modify()
            else:
                print("No cross found.")
        else:
            print("Invalid input. Try again.")

while 1:
    print("1. Trucks")
    print("2. Cars")
    print("3. Motorbikes")
    print("99. Exit menu")
    choice=int(input("Please choose a number from the menu where you want to go to: "))

    if choice==99:
        break
    elif choice==1:
        add_truck()
    elif choice==2:
        add_car()
    elif choice==3:
        add_motorbike()
    else:
        print("Invalid input. Try again.")


