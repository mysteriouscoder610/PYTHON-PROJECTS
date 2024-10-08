from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="light blue")

lab = Label(sp, text="INTERNET SPEED TEST", font=("Times New Roman", 20, "bold"), bg="Light blue", fg="dark blue")
lab.place(x=40, y=40, height=50, width=380)

lab = Label(sp, text="Downloading speed", font=("Times New Roman", 30, "bold"), bg="light blue", fg="dark blue")
lab.place(x=40, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"), fg="dark blue")
lab_down.place(x=40, y=200, height=50, width=380)

lab = Label(sp, text="Uploading speed", font=("Times New Roman", 30, "bold"), bg="light blue", fg="dark blue")
lab.place(x=40, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"), fg="dark blue")
lab_up.place(x=40, y=360, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="dark blue", fg="white", command=speedcheck)
button.place(x=40, y=460, height=50, width=380 )



sp.mainloop()
