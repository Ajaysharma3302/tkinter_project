from tkinter import *
from tkcalendar import *
root=Tk()
root.title("Calender")
root.geometry("400x600")
cal=Calendar(root,selectmode="day",year=2023,month=7,day=26)
cal.pack(pady=20)
def grab_date():
    my_label.config(text=cal.get_date())
my_button=Button(root,text="Get Date",command=grab_date)
my_button.pack(pady=20) 
my_label=Label(root,text=" ")
my_label.pack(pady=20)


root.mainloop()
   