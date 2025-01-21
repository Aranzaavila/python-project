import tkinter as tk
from tkinter import messagebox
import random
import json 


#reads data from json file 
try:
    with open("data.json", "r") as file:
        data= json.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "File not found")
    exit()

warm= data["warm"]
cold= data["cold"]
activities= data["activities"]


#define functions 
selected_country= ""
def weather_place(weather_type):
    global selected_country
    if weather_type == "warm":
        selected_country = random.choice(warm)
    else:
        selected_country = random.choice(cold)
    
    label_result.config(text=f"Your next trip will be in: {selected_country}")
    button_activities.config(state="normal")

def show_activities():
 if selected_country in activities:
        activities_list= activities [selected_country]
        activities_str= "\n".join([f'{i+1}. {act}' for i, act in enumerate(activities_list)])
        messagebox.showinfo(f"Activities in {selected_country}", f"Popular activities in {selected_country}:\n\n{activities_str}")
 else:
        messagebox.showwarning("No activities", f"No activities found for {selected_country }")

def changeBG():
    window.config(background= "red")
def exit_game():
 window.destroy()
    

#GUI window

window= tk.Tk()
window.title("Random destination game")
window.geometry("500x500")
window.config(background= "#f7f0dc")

bg= PhotoImage(file="bg.png")


#creates label widgets
label_intro= tk.Label(window, text= "Welcome to the game!", font=("Impact", 40, "bold"), fg="#0a6121", bg= "#91eda3", width=20, height=2)
label_intro.pack()

label_desicion= tk.Label(window, text="Choose the type of weather for your vacation:", font=("Arial", 12, "bold"), bg="#91eda3", fg="#0a6121" )
label_desicion.pack(pady=10, padx=10)

frame_buttons= tk.Frame(window, bg= "#f7f0dc")
frame_buttons.pack(pady=22, padx=10)

button_warm= tk.Button(frame_buttons, text= "🌞Warm🌞",bg= "#ed7272", fg="black", font=("Arial", 12, "bold"), command= lambda: weather_place("warm")) 
button_warm(command=changeBG)
button_warm.grid(row=0, column=0, padx=10, pady=10)
button_cold= tk.Button(frame_buttons, text="❄️Cold❄️", fg= "white", bg="#8092ed", font=("Arial", 12, "bold"), command= lambda: weather_place("cold") )
button_cold.grid(row=0, column=1, padx=10, pady=10)

label_result= tk.Label(window, text= "Your next trip will be in:", fg="#0a6121", bg="#91eda3", font=("Arial", 12, "bold"), pady=10)
label_result.pack()
 

button_activities= tk.Button(window, text="Show activities", font=("Arial", 12), bg="#91eda3", fg="#0a6121", state= "disabled", command=show_activities)
button_activities.pack(pady=10)


button_exit= tk.Button(window, text="Exit",font=("Arial", 12, "bold"), bg="gray", fg="black", command=exit_game)
button_exit.pack(pady=10)


window.mainloop()
