import tkinter as tk
from tkinter import messagebox
import random


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





#GUI window
window= tk.Tk()
window.title("Random destination game")
window.geometry("400x500")
window.config(background= "#a6ffe4")

#labels
photo= tk.PhotoImage(file="welcome.png")
label_intro= tk.Label(window,
                  text= "Welcome to the game!",
                  font=("Arial", 30), 
                  fg="#0a0a57",
                  image= photo,
                  compound= "bottom")
label_intro.pack()

label_desicion= tk.Label(window, text="Choose the type of weather for yout vacation:",
                      font=("Arial, 12"))
label_desicion.pack()
       
window.mainloop()