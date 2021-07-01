from tkinter import *

widthofFrame=1280
heightofFrame=840

#[+] Initialize Window[+]
ip_tracker=Tk() 
ip_tracker.geometry(str(widthofFrame) +'x' + str(heightofFrame))


e = Entry(ip_tracker, width=50, borderwidth=5)


e.pack()


def myclick():
    label1= Label(ip_tracker, text=e.get())
    label1.pack()





#[+] Create Label [+]
mainInterfaceLabel = Label(ip_tracker, text="IP Tracker")


#[+] Pack the Label into the Window [+]
mainInterfaceLabel.pack()

mybutton = Button(ip_tracker, text= "Enter your Name", command=myclick,padx=25 ,pady=25)
mybutton.pack()

ip_tracker.mainloop()
 