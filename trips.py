def countries():
    while True:
        print("Choose the type of weather you would like to have in your vacation")
        print("\n 1 - Cold weather \n 2 - Warm weather")

        choice= int(input("Enter your choice: "))

        while choice > 2 or choice < 1:
            choice = int(input("Enter a valid choice: "))
        
        if choice == "1":

 

   