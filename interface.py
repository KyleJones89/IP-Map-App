import tkinter

#[+] Initialize Window[+]
ip_tracker=tkinter.Tk() 

#[+] Create Label [+]
mainInterfaceLabel = tkinter.Label(ip_tracker, text="IP Tracker")

#[+] Pack the Label into the Window [+]
mainInterfaceLabel.pack()

ip_tracker.mainloop()
 