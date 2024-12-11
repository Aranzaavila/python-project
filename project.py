import random 

warm = ["Mexico", "Venezuela"]

cold = ["Canada", "Russia"]

def choose_warm(warm):
    print(f"You should go to: {random.choice(warm)}")

def choose_cold(cold):
    return random.choice(cold)

def activities_countries(country):
    activities = {
    "Mexico": ["Xcaret", "Chichen Itza ", ""],
    "Venezuela": ["Thundering Angel Falls", "Tucacas", "Isla de Margarita (Margarita Island)", ""],
    "Canada": ["Niagara Fall", "Banff National Park & the Rocky Mountains", "Stanley Park", "Notre-Dame Basilica", "Toronto's CN Tower", "St. John's Signal Hill National Historic Site"],
    "Russia": ["Red Square",  "Kremlin", "Novodevichy Convent", "Christ the Saviour Cathedral", "Kolomenskoe Estate", "Arbat street and Victory Park"]
}
    return activities.get(country)
    

def main():
    while True:
        print("")
        print("Choose the type of weather you would like to have in your vacation")
        print("1. warm")
        print("2. cold")
        print("3. Exit")
        print("")
        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                choose_warm(warm)
                if warm:
                    user_answer = input("Do you wanna know the activities about this country? (yes/no): ").strip().lower()
                    if user_answer == "yes":
                        country_activities = input("Write the name of the country, please: ").capitalize().strip()
                        
                        activities = activities_countries(country_activities)
                        print(f"\n Popular activities in {country_activities}:")
                        for i, activities in enumerate(activities, start=1):
                            print(f"{i}. {activities}")
                        break
                    
                    elif user_answer == "no":
                        print("Bye bye!")
                        break
                    else:
                        print("Input not valid, please enter (yes/no).")
                        print("")
                else:
                    continue


            elif choice == 2:
                choose_cold(cold)
                result = print(f"You should go to: {cold}")

            elif choice == 3:
                print("Thanks for all!")
                print("Hope to see you soon.")
                print("")
                break

            else:
                print("Type a valid input")
                print("")
        except ValueError:
           print("Input not valid, try again.")
           print("")

main()
