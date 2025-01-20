import tkinter as tk
from tkinter import messagebox
import random
import json 


warm = ["Mexico", "Venezuela", "Spain", "Dominican Republic", "Portugal"]
cold = ["Canada", "Russia", "Finland", "Norway", "Iceland"]

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


#define functions 

def weather_place(weather_type):
    if weather_type == "warm":
        selected_country = random.choice(warm)
    else:
        selected_country = random.choice(cold)
    
    label_result.config(text=f"You should go to {selected_country}")
    button_activities.config(state="normal")

def show_activities():
 if selected_country in activities:
        activities_list= activities [selected_country]
        activities_str= "\n".join([f'{i+1}. {act}' for i, act in enumerate(activities_list)])
        messagebox.showinfo(f"Activities in {selected_country}", f"Popular activities in {selected_country}:\n\n{activities_str}")
 else:
        messagebox.showwarning("No activities", f"No activities found for {selected_country }")


def exit_game():
 window.destroy()
    

#GUI window

window= tk.Tk()

window.title("Random destination game")
window.geometry("400x500")
window.config(background= "#a6ffe4")

#creates label widgets
photo= tk.PhotoImage(file="vacation.png")

label_intro= tk.Label(window, text= "Welcome to the game!", font=("Arial", 30), fg="#0a0a57", image= photo, compound= "bottom")
label_intro.pack()


label_desicion= tk.Label(window, text="Choose the type of weather for yout vacation:", font=("Arial, 12"))
label_desicion.pack()

frame_buttons= tk.Frame(window)
frame_buttons.pack(pady=10, padx=5)

button_warm= tk.Button(frame_buttons, text= "Warm", font=("Arial", 12), command=lambda: weather_place("warm")) 
button_warm.grid(row=0, column=1, padx=10)
button_cold= tk.Button(frame_buttons, text="Cold", font=("Arial", 12), command= lambda: weather_place("cold") )
button_cold.grid(row=0, column=2, padx=10)



label_result= tk.Label(window, text= "Show activities", font=("Arial", 12), pady=10)
label_result.pack()

 

button_activities= tk.Button(window, text="Show activities", font=("Arial", 12), state= "disabled", command=show_activities)
button_activities.pack(pady=5)


button_exit= tk.Button(window, text="Exit",font=("Arial", 12), command=exit_game)
button_exit.pack(pady=5)






window.mainloop()
