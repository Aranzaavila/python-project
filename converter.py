

def converter():

    weight= float(input("Enter the weight: "))
    unit= input("Convert pounds to kilograms or kilograms to pounds? : ")

    if unit == "pounds to kilograms":
        print(weight / 2.205, "kg" )
        
    elif unit == "kilograms to pounds":
        print(weight * 2.205, "lbs" )
        
    else:
        print("not valid")


converter()