from tkinter import Tk
import random

warm = ["Mexico", "Venezuela", "Spain", "Dominican Republic", "Portugal"]
cold = ["Canada", "Russia", "Finland", "Norway", "Iceland"]

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
    
def weather_place(weather_type):
    if weather_type== "warm":
        country= random.choice(warm)
    elif weather_type== "cold":
       country= random.choice(cold)



root= Tk()
root.title("Random destination game")
root.geometry("400x500")

       
root.mainloop()
