from tkinter import *
pizza = Tk()
from PIL import ImageTk, Image


#adds company name at top
company = Label(pizza, text="Parker's Pizza")
company.grid(row=0, column= 5)

#adds a picture of a cheese pizza on the left
cheese_picture = ImageTk.PhotoImage(Image.open("cheese.png"))
pic_lbl = Label(pizza, image=cheese_picture)
pic_lbl.grid(row=3, column=0)

#adds a picture of a pepperoni pizza on the right
pepperoni_picture = ImageTk.PhotoImage(Image.open("pepp.png"))
pic_lbl = Label(pizza, image=pepperoni_picture)
pic_lbl.grid(row=3, column=10)

#adds a list of the pizza options in the center
my_pizza_list = ["16 inch pepp - $18", "12 inch pepp - $14", "16 inch cheese - $16", "12 inch cheese - $12"]

pizza_list = Listbox(pizza, selectmode=MULTIPLE)
pizza_list.grid(row=5, column=5)


for item in my_pizza_list:
    pizza_list.insert(0, item)


#buttons to add pizza to the cart, delete the cart, and checkout
def addPizza():
    labels = []
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"
        add_lbl.config(text="Cart: " + "\n" + result)
        
def deletePizza():
        add_lbl.destroy()
             

add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=8)


addPizza = Button(pizza, text="Add to cart", command = addPizza)
addPizza.grid(row=6, column=5)

deletePizza = Button(pizza, text="Delete cart", command = deletePizza)
deletePizza.grid(row=7, column=5)


checkOut = Button(pizza, text="Check Out")
checkOut.grid(row=8, column=5)




pizza.mainloop()
