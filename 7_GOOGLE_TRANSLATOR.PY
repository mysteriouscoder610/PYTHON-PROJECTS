from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text  # Return the translated text, not the object

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)  # Use 1.0 to delete from start
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='Grey')

label_t = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
label_t.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Grey")
lab.place(x=100, y=100, height=50, width=300)

Sor = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor.place(x=10, y=150, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("English")

lab = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Grey")
lab.place(x=100, y=360, height=20, width=300)

dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
