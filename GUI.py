#import required libraries
import tkinter as tk #library for GUI 
from tkinter import messagebox #displays message to user
import random #selects reandom destinations
import json #reads data from a JSON file 

#reads data from json file 
try:
    with open("data.json", "r") as file:
        data= json.load(file) #loads JSON data 
except FileNotFoundError:
    messagebox.showerror("Error", "File not found") # Show an error message if the file is not found and exit the program
    exit()
#extracts data from the JSON file
warm= data["warm"]
cold= data["cold"]
activities= data["activities"]


#define functions 
selected_country= "" #stores the selected destination
def weather_place(weather_type):
    """
    Selects a random destination based on the chosen weather type (warm or cold).
    Updates the result label with the selected destination.
    Enables the 'Show activities' button.
    """
    global selected_country
    if weather_type == "warm":
        selected_country = random.choice(warm)
    else:
        selected_country = random.choice(cold)
    #gives an update to the label to display the selected destination
    label_result.config(text=f"Your next trip will be in: {selected_country}")
    #unlocks the activities button
    button_activities.config(state="normal")

def show_activities():
    """
    Displays popular activities for the selected destination in a message box.
    If no activities are found, shows a warning message.
    """
    if selected_country in activities:
        activities_list= activities [selected_country]
        activities_str= "\n".join([f'{i+1}. {act}' for i, act in enumerate(activities_list)])  #format the activities list for display
        messagebox.showinfo(f"Activities in {selected_country}", f"Popular activities in {selected_country}:\n\n{activities_str}") #show the activities in a message box
    else:
        messagebox.showwarning("No activities", f"No activities found for {selected_country }") #show a warning if no activities are found

def exit_game():
    """
    Closes the application window.
    """
    window.destroy()

#GUI window
window= tk.Tk() #creates the main application window
window.title("Random destination game")
window.geometry("900x600")
window.config(background= "#f7f0dc")


#creates and pack the introductory label
label_intro= tk.Label(window, text= "Welcome to the game!", font=("Impact", 40, "bold"), fg="#0a6121", bg= "#91eda3", width=20, height=2)
label_intro.pack()
#create and pack the weather choice instruction label
label_desicion= tk.Label(window, text="Choose the type of weather for your vacation:", font=("Arial", 25, "bold"), bg="#91eda3", fg="#0a6121" )
label_desicion.pack(pady=10, padx=10)

#create a frame to hold the weather buttons
frame_buttons= tk.Frame(window, bg= "#f7f0dc")
frame_buttons.pack(pady=22, padx=10)

#warm weather button
button_warm= tk.Button(frame_buttons, text= "🌞Warm🌞",bg= "#ed7272", fg="black", font=("Arial", 20, "bold"), command= lambda: weather_place("warm")) 
button_warm.grid(row=0, column=0, padx=10, pady=10)
#cold weather button
button_cold= tk.Button(frame_buttons, text="❄️Cold❄️", fg= "white", bg="#8092ed", font=("Arial", 20, "bold"), command= lambda: weather_place("cold") )
button_cold.grid(row=0, column=1, padx=10, pady=10)

#displays the selected destination
label_result= tk.Label(window, text= "Your next trip will be in:", fg="#0a6121", bg="#91eda3", font=("Arial", 21, "bold"), pady=10)
label_result.pack()
 
#button to show activities
button_activities= tk.Button(window, text="Show activities", font=("Arial", 21), bg="#91eda3", fg="#0a6121", state= "disabled", command=show_activities)
button_activities.pack(pady=10)

#exit button to close the application
button_exit= tk.Button(window, text="Exit",font=("Arial", 18, "bold"), bg="gray", fg="black", command=exit_game)
button_exit.pack(pady=10)

#start the main event loop
window.mainloop()
