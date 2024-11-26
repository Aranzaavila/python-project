
while True:
    input("Welcome!, with this calculator you will be able to know your body mass index and the minimun amount of calories your body needs in one day, press enter to continue ")
    

    #Formula to calculate BMI
    gender= str(input("What is your gender? (male or female)"))
    height= float(input("What is your height in m?"))
    weight= float(input("What is your weight in kg?"))
    age= int(input("How old are you?"))
    BMI = weight / (height ** 2) 
    print( " This is your BMI:  ", BMI)
       
    if BMI < 18.5:
     print("You are underweight")
    elif BMI <= 24.9: 
     print ("You are in a normal weight!")
    elif BMI <= 29.9:
     print("You are overweight")
    else:
     print("You have obesity")


    #Calculate BMR (Basal Metabolic Rate) 
    if gender == "male":
        BMR_men= print(" The minimun of calories that your body needs in one day are: ", 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age))
    else:
        BMR_women= print(" The minimun of calories that your body needs in one day are: ", 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age))
    
    