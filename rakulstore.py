"""

A program that maintains the stock of a decoration shop
Item_Name,Price_code
Quantity,Dealer_name

user can:
view all items
search an item
add item
update item
delete
close

"""

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=box.curselection()[0]
    selected_tuple = box.get(index)
    e_itemname.delete(0,END)
    e_itemname.insert(END,selected_tuple[1])
    e_pricecode.delete(0,END)
    e_pricecode.insert(END,selected_tuple[2])
    e_quantity.delete(0,END)
    e_quantity.insert(END,selected_tuple[3])
    e_dealername.delete(0,END)
    e_dealername.insert(END,selected_tuple[4])

def view_command():
    box.delete(0,END)
    for row in backend.view():
        box.insert(END,row)

def search_command():
    box.delete(0,END)
    for row in backend.search(item_text.get(),price_text.get(),quantity_text.get(),dealer_text.get()):
        box.insert(END,row)

def add_command():
    backend.insert(item_text.get(),price_text.get(),quantity_text.get(),dealer_text.get())
    box.delete(0,END)
    box.insert(END,(item_text.get(),price_text.get(),quantity_text.get(),dealer_text.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=box.curselection()[0]
        selected_tuple = box.get(index)
        e_itemname.delete(0,END)
        e_itemname.insert(END,selected_tuple[1])
        e_pricecode.delete(0,END)
        e_pricecode.insert(END,selected_tuple[2])
        e_quantity.delete(0,END)
        e_quantity.insert(END,selected_tuple[3])
        e_dealername.delete(0,END)
        e_dealername.insert(END,selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],item_text.get(),price_text.get(),quantity_text.get(),dealer_text.get())


window = Tk()

window.wm_title("Lakshmi Paper Stores")


l_itemname = Label(window,text = "Item_Name")
l_itemname.grid(row = 0,column = 0)

l_pricecode = Label(window,text = "Price_code")
l_pricecode.grid(row = 0,column = 2)

l_quantity = Label(window,text = "Quantity")
l_quantity.grid(row = 1,column = 0)

l_dealername = Label(window,text = "Dealer_name")
l_dealername.grid(row = 1,column = 2)

item_text = StringVar()
e_itemname =Entry(window,textvariable = item_text)
e_itemname.grid(row=0,column=1)

price_text = StringVar()
e_pricecode =Entry(window,textvariable = price_text)
e_pricecode.grid(row=0,column=3)

quantity_text = StringVar()
e_quantity =Entry(window,textvariable = quantity_text)
e_quantity.grid(row=1,column=1)

dealer_text = StringVar()
e_dealername =Entry(window,textvariable = dealer_text)
e_dealername.grid(row=1,column=3)

box = Listbox(window,height = 6,width = 35)
box.grid(row = 2,column = 0,rowspan = 6,columnspan = 2 )

sbar = Scrollbar(window)
sbar.grid(row = 2,column = 2,rowspan = 6)

box.configure(yscrollcommand=sbar.set)
sbar.configure(command = box.yview)

box.bind('<<ListboxSelect>>',get_selected_row)

b_view = Button(window,text="View_All",width = 12,command = view_command)
b_view.grid(row = 2,column = 3)

b_search = Button(window,text="search",width = 12,command = search_command)
b_search.grid(row = 3,column = 3)

b_add = Button(window,text="Add",width = 12,command = add_command)
b_add.grid(row = 4,column = 3)

b_update = Button(window,text="Update",width = 12,command = update_command)
b_update.grid(row = 5,column = 3)

b_delete = Button(window,text="Delete",width = 12,command = delete_command)
b_delete.grid(row = 6,column = 3)

b_close = Button(window,text="Close",width = 12,command = window.destroy)
b_close.grid(row = 7,column = 3)


window.mainloop()
