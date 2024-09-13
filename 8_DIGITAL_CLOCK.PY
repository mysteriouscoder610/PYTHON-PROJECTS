from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    # we are using after and it will change the data in each box
    # with a specific rate 
    lab_hr.after(200,date_time)

clock = Tk()
# graphics upar aur mainloop wale line ke bich me lagega
clock.title(' ****Digital Clock****')
clock.geometry('1000x500')
clock.config(bg='light blue')
# Now how to make small small blocks

# Time section starts

lab_hr = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_txt = Label(clock,text="Hour", font=('Book Antiqua',30,"bold"),
               bg='dark blue',fg="white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_txt = Label(clock,text="Minute", font=('Book Antiqua',20,"bold"),
               bg='dark blue',fg="white")
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt = Label(clock,text="Sec. ", font=('Book Antiqua',30,"bold"),
               bg='dark blue',fg="white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_am = Label(clock,text="00", font=('Book Antiqua',40,"bold"),
               bg='dark blue',fg="white")
lab_am.place(x=780,y=50,height=110,width=100)

lab_am_txt = Label(clock,text="AM/PM", font=('Book Antiqua',20,"bold"),
               bg='dark blue',fg="white")
lab_am_txt.place(x=780,y=190,height=40,width=100)

# Date section starts 

lab_date = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_txt = Label(clock,text="Date", font=('Book Antiqua',30,"bold"),
               bg='dark blue',fg="white")
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_mon = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_mon.place(x=340,y=270,height=110,width=100)

lab_mon_txt = Label(clock,text="Month", font=('Book Antiqua',20,"bold"),
               bg='dark blue',fg="white")
lab_mon_txt.place(x=340,y=410,height=40,width=100)

lab_year = Label(clock,text="00", font=('Book Antiqua',60,"bold"),
               bg='dark blue',fg="white")
lab_year.place(x=560,y=270,height=110,width=100)

lab_year_txt = Label(clock,text="Year", font=('Book Antiqua',30,"bold"),
               bg='dark blue',fg="white")
lab_year_txt.place(x=560,y=410,height=40,width=100)

lab_day = Label(clock,text="00", font=('Book Antiqua',30,"bold"),
               bg='dark blue',fg="white")
lab_day.place(x=780,y=270,height=110,width=100)

lab_day_txt = Label(clock,text="Day", font=('Book Antiqua',20,"bold"),
               bg='dark blue',fg="white")
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()

clock.mainloop()  
# above line makes the graphic on



