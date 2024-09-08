import turtle
import pandas as pd
import tkinter 
from tkinter import messagebox

# csv dosyası

data = pd.read_csv("countries_coor.csv")

# image ve ekran ayarlari

screen = turtle.Screen()
screen.title("Kaç Tane Avrupa Ülkesi İsmi Sayabilirsin?")
screen.bgcolor("gray")

image = "blank_countries.gif"

screen.addshape(image)
turtle.shape(image)

# oyun

all_countries = data.country.to_list()
guessed_countries = []


while len(guessed_countries) < 49:
    
    answer = screen.textinput(title = f"{len(guessed_countries)}/49 Ülke", prompt= "Ülke Adı Giriniz:").title()
    
    if answer == "Exit":
        # tkinter penceresini gizli hale getirin
        root = tkinter.Tk()
        root.withdraw()  # tkinter ana penceresini gizle
        screen.bye()    
        messagebox.showinfo("Oyun Bitti",f"Skor: {len(guessed_countries)}/49")
        root.destroy()
        break

    if answer in all_countries:
        guessed_countries.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer]
        t.goto(country_data.x.item(),country_data.y.item())
        t.write(answer)
    
screen.exitonclick()

    
'''
#ulkelerin koordinatlarini bulmak icin:

def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''