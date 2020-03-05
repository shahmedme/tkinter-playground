from tkinter import *
from tkinter import ttk, scrolledtext, messagebox

# SETTING UP WINDOW
window = Tk()
window.title("Tkinter Dekstop App")
# window.geometry('900x250')

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

# SCROLLED TEXT
textarea = scrolledtext.ScrolledText(window, width=40, height=10)
textarea.grid(row=6, column=0)


# SPINBOX
spinbox = Spinbox(window, from_=0, to=100, width=5)
spinbox.grid(row=8, column=0)


# FUNCTIONS TO ACT CHANGES
def change_text():
    msg = txt.get()
    lbl.configure(text=msg)


def clicked():
    msg = "Clicked"
    lbl.configure(text=msg)


def show_alert():
    messagebox.showinfo('this is title', 'thanks for clicking')
    messagebox.showerror('error', 'something went wrong')
    messagebox.showwarning('warning', 'you have been warned')


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

btn2 = Button(window, text="Show Alert", bg='black', fg='white', command=show_alert)
btn2.grid(row=7, column=0)


def ask_yes_no():
    msg = messagebox.askyesno('title', 'content')


btn3 = Button(window, text="Ask Yes No", command=ask_yes_no)
btn3.grid(row=7, column=1)


def ask_yes_no_cancel():
    msg = messagebox.askyesnocancel('title', 'content')


btn4 = Button(window, text="Ask Yes No Cancel", command=ask_yes_no_cancel)
btn4.grid(row=7, column=2)


def ask_ok_cancel():
    msg = messagebox.askokcancel('title', 'content')


btn5 = Button(window, text="Ask Ok Cancel", command=ask_ok_cancel)
btn5.grid(row=7, column=3)


def ask_retry_cancel():
    msg = messagebox.askretrycancel('title', 'content')


btn6 = Button(window, text="Ask Retry Cancel", command=ask_retry_cancel)
btn6.grid(row=7, column=4)

window.mainloop()
