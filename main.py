from tkinter import *
from tkinter import ttk

# SETTING UP WINDOW
window = Tk()
window.title("Tkinter Dekstop App")
window.geometry('900x250')

# LABEL
lbl = Label(window, text="Shakil Ahmed", font=('Verdana', 50))
lbl.grid(row=1, column=0)

# INPUT BOX
txt = Entry(window, width=50)
txt.focus()
txt.grid(row=0, column=0)

txt2 = Entry(window, width=50, state='disabled')
txt2.grid(row=0, column=1)

# DROPDOWN BOX
combo = ttk.Combobox(window)
combo['values'] = ("S&M", "Web", "AI", "...")
combo.current(3)
combo.grid(row=3, column=0)

# CHECKBOX
state = BooleanVar()
state.set(True)
cb = Checkbutton(window, text='Choose', var=state)
cb.grid(row=4, column=0)


# FUNCTIONS TO ACT CHANGES
def change_text():
    msg = txt.get()
    lbl.configure(text=msg)


def clicked():
    msg = "Clicked"
    lbl.configure(text=msg)


# RADIO BUTTON
rad1 = Radiobutton(window, text='First', value=1, command=clicked)
rad2 = Radiobutton(window, text='Second', value=2, command=clicked)
rad3 = Radiobutton(window, text='Third', value=3, command=clicked)

rad1.grid(row=5, column=1)
rad2.grid(row=5, column=2)
rad3.grid(row=5, column=3)

# BUTTON
btn = Button(window, text="Click Me", bg="orange", fg="white", command=change_text)
btn.grid(row=0, column=2)

window.mainloop()
