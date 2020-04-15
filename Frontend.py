from tkinter import *
from Backend import Database

db = Database("booksDB.db")

def get_selected_row(event):
    try:
        global selected_row
        index = listbox.curselection()[0]
        selected_row = listbox.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_row[1])
        e2.delete(0,END)
        e2.insert(END, selected_row[2])
        e3.delete(0,END)
        e3.insert(END, selected_row[3])
        e4.delete(0,END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass
    
def view_command():
    listbox.delete(0,END)
    for row in db.view():
        listbox.insert(END, row)

def search_command():
    listbox.delete(0,END)
    for row in db.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        listbox.insert(END, row)

def add_command():
    db.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    listbox.delete(0,END)
    listbox.insert(END,(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))

def update_command():
    db.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())

def delete_command():
    db.delete(selected_row[0])

def close_command():
    window.destroy()

window = Tk()

window.wm_title('Bookshelf')

l1 = Label(window, text='Title')
l1.grid(row=0,column=0)

l2 = Label(window, text='Author')
l2.grid(row=0,column=2)

l3 = Label(window, text='Year')
l3.grid(row=1,column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1,column=3)

listbox = Listbox(window, height=6, width=45)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

scrollBar = Scrollbar(window)
scrollBar.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='View all', width=17, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry', width=17, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry', width=17, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=17, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=17, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=17, command=close_command)
b6.grid(row=7, column=3)

window.mainloop()