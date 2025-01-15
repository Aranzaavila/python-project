from tkinter import Tk
import random 
game= Tk()
game.title("Random destination game")
game.size("400x500")

warm = ["Mexico", "Venezuela", "Spain", "Dominican Republic", "Portugal"]

cold = ["Canada", "Russia", "Finland", "Norway", "Iceland"]

def choose_warm(warm):
    print(f"You should go to: {random.choice(warm)}")

def choose_cold(cold):
    print(f"You should go to: {random.choice(cold)}")

def activities_countries(country):
    activities = {
    "Mexico": ["Xcaret", "Chichen Itza ", "The Chapultepec Castle", "Great Pyramid of Cholula", "Tulum Ruins", "Monte Alban"],
    "Venezuela": ["Thundering Angel Falls", "Tucacas", "Isla de Margarita (Margarita Island)", "Morrocoy National Park)", "Canaima National Park and the Gran Sabana", "Roraima"],
    "Spain": ["The Sagrada Familia", "Alhambra Palace Granada","The Royal Palace Madrid","Seville Cathedral","Santiago de Compostela Cathedral","Costa de la Luz Beaches" ],
    "Dominican Republic" : ["Bavaro Beach","Saona Island","Hoyo Azul","Los Haitises National Park","Macao Beach","Fort San Felipe"],
    "Portugal": ["The Douro Valley","Mosteiro de Santa Maria da Vitória","Convento de Cristo","Belém Tower","São Jorge Castle","Dom Luís I Bridge"],
    "Finland": ["Sea Fortress Suomenlinna","Temppeliaukio Church","Santa Claus Village","Old Market Hall","Seurasaaren Ulkomuseo","Arktikum"],
    "Norway": ["The Vigeland Park","The Vigeland Park","Bryggen","Viking Ship Museum","Pulpit Rock","Frognerparken"],
    "Iceland": ["Blue Lagoon","Thingvellir National Park","Hallgrimskirkja","Perlan","Gullfoss Falls","Jökulsárlón"],
    "Canada": ["Niagara Fall", "Banff National Park & the Rocky Mountains", "Stanley Park", "Notre-Dame Basilica", "Toronto's CN Tower", "St. John's Signal Hill National Historic Site"],
    "Russia": ["Red Square",  "Kremlin", "Novodevichy Convent", "Christ the Saviour Cathedral", "Kolomenskoe Estate", "Arbat street and Victory Park"]
}
    return activities.get(country)
    

def main():
    while True:
        print("Welcome to random destination game! Lets get started!")
        print("")
        print("Choose the type of weather you would like to have in your vacation")
        print("1. warm")
        print("2. cold")
        print("3. Exit")
        print("")
        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                choose_warm(warm) #
                if warm:
                    user_answer = input("Do you wanna know the activities about this country? (yes/no): ").strip().lower()
                    if user_answer == "yes":
                        country_activities = input("Write the name of the country, please: ").capitalize().strip()
                        
                        #
                        activities = activities_countries(country_activities)
                        print(f"\n Popular activities in {country_activities}:")
                        for i, activities in enumerate(activities, start=1):
                            print(f"{i}. {activities}")
                        
                        print("Thanks for playing!")
                        print("-------------------------------------")

                        new_game= input("Press 'r' to restart or 'e' to end it: ")
                        if new_game == "r":
                            continue
                        else:
                            print("Thanks for playing!")
                            break
                         
            
                    elif user_answer == "no":
                        print("Bye bye!")
                        break
                    else:
                        print("Input not valid, please enter (yes/no)")
                        print("")
                else:
                    continue

                


            elif choice == 2:
                choose_cold(cold)
                if cold: 
                    user_answer = input("Do you want to knnow the activities about this country? yes/no: ").strip().lower()
                    if user_answer == "yes":
                        country_activities = input("Write the name of the country, please: ").capitalize().strip()
                        
                        activities = activities_countries(country_activities)
                        print(f"\n Popular activities in {country_activities}:")
                        for i, activities in enumerate(activities, start=1):
                            print(f"{i}. {activities}")
                        
                        print("Thanks for playing!")
                        print("-------------------------------------")

                        new_game= input("Press 'r' to restart or 'e' to end it: ")
                        if new_game == "r":
                            continue
                        else:
                            print("Thanks for playing!")
                            break 

                        
                    
                    elif user_answer == "no":
                        print("Bye bye!")
                        break
                    else:
                        print("Input not valid, please enter (yes/no):")
                        print("")
                else:
                    continue
                        

            

            elif choice == 3:
                print("What a shame! :(")
                print("Hope you play soon")
                print("")
                break

            else:
                print("Type a valid input")
                print("")
        except ValueError:
           print("Input not valid, try again.")
           print("")
  
main()

game.mainloop()