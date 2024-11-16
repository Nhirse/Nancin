

def get_inputs():
    name=input("What's your name")
    water=int(input("How many units of water do you want?"))
    electric = int(input("How many units of electric do you want?"))
    gas = int(input("How many units of gas do you want?"))

    gas_fee=3.6*gas
    electric_fee=2.2*electric
    water_fee=1.4*water
    all_taxes=(gas_fee+electric_fee+water_fee)*0.8
    total_amount=all_taxes+gas_fee+electric_fee+water_fee


dict={"person 1":
          {"Name": "Ahmed",
           "Water": 29,
           "Gas": 23,
           "Electric": 35},
      }
while 1:
    print("1. Add a person")
    print("2. Delete a person")
    print("3. Modify information")
    print("4. Display all people")
    print("5. Exit the menu")
    select=int(input(("Welcome. Choose the number for what you'd like to do")))
    if select==5:
        break
    elif select==1:
        get_inputs()
    elif select==2:
