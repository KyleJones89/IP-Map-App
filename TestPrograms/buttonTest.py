import tkinter






def myclick():
    label1= tkinter.Label(ip_tracker, text="Button Clicked")
    label1.pack()



#[+] Initialize Window[+]
ip_tracker=tkinter.Tk() 

#[+] Create Label [+]
mainInterfaceLabel = tkinter.Label(ip_tracker, text="IP Tracker")


#[+] Pack the Label into the Window [+]
mainInterfaceLabel.pack()

mybutton = tkinter.Button(ip_tracker, text= "Click Me!", command=myclick,padx=25 ,pady=25)
mybutton.pack()

ip_tracker.mainloop()
 