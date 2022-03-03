from tkinter import *
pizza = Tk()
from PIL import ImageTk, Image

company = Label(pizza, text="Parker's Pizza")
company.grid(row=0, column= 5)

cheese_picture = ImageTk.PhotoImage(Image.open("cheese.png"))
pic_lbl = Label(pizza, image=cheese_picture)
pic_lbl.grid(row=3, column=0)


pepperoni_picture = ImageTk.PhotoImage(Image.open("pepp.png"))
pic_lbl = Label(pizza, image=pepperoni_picture)
pic_lbl.grid(row=3, column=10)

my_cheese_list = ["16 inch cheese - $16", "12 inch cheese - $12"]

cheese_list = Listbox(pizza)
cheese_list.grid(row=5, column=0)


for item in my_cheese_list:
    cheese_list.insert(0, item)


my_pep_list = ["16 inch peperoni - $18", "12 inch peperoni - $14"]

pep_list = Listbox(pizza)
pep_list.grid(row=5, column=10)

for item in my_pep_list:
    pep_list.insert(0, item)



def add_cheese():
    result = ""
    for item in cheese_list.curselection():
        result = result + str(cheese_list.get(item)) + "\n"

        add_lbl.config(text="Cart: " + "\n" + result)

def add_pep():
    result = ""
    for item in pep_list.curselection():
        result = result + str(pep_list.get(item)) + "\n"

        add_lbl.config(text="Cart: " + "\n" + result)


add_lbl = Label(pizza, text="")
add_lbl.grid(row=8, column=5)


add_button = Button(pizza, text="Add to cart", command = add_cheese)
add_button.grid(row=6, column=0)

add_button = Button(pizza, text="Add to cart", command = add_pep)
add_button.grid(row=6, column=10)







pizza.mainloop()
