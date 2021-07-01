from tkinter import *
import tkinter


#[+] Definitions Pane[+]





#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################



#[+] Initialize Window[+]
ip_tracker=Tk() 
#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################

#{+}Frame building and placement{+}
topframe= Frame(ip_tracker,width=450,height=50,pady=3).grid(row=0,column=0,rowspan=4,columnspan=9)

bottomFrame=Frame(ip_tracker,width=450,height=50,pady=3).grid(row=4, column= 0,rowspan=6,columnspan=9)

#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################



labelforEntry1 = Label(topframe,text="Enter IP Address: ")
labelforEntry1.grid(row = 0,column = 0)

entry1 = Entry(topframe, width = 50, borderwidth = 5)
entry1.grid(row = 0, column = 1)



labelforEntry2 = Label(topframe, text="Enter Name of System: ")
labelforEntry2.grid(row = 0,column = 2)
entry2 = Entry(topframe, width = 50, borderwidth = 5)
entry2.grid(row = 0, column = 3)


def checkifEntryEmpty(entry): #If entry is empty, return true
    if len(entry.get()) == 0:
        return True
    else:
        return False



def crossReferenceTwoBoxesEmpty(boolvalue1, boolvalue2):

    if(boolvalue1 == True or boolvalue2 == True ):
        return True
    else:
        return False

def displayEntryBoxData(varentry1,varentry2):
    if(crossReferenceTwoBoxesEmpty(checkifEntryEmpty(varentry1),checkifEntryEmpty(varentry2))==False):
        returnvalue= str(varentry1.get()+" "+str(varentry2.get()))
        
        return returnvalue
    else:
        return "This is a bad input"


def myclick():
    
    mylabel = Label(topframe, text=displayEntryBoxData(entry2,entry1))
    
    mylabel.grid(row=2,column=2)
    

    

buttonTest = Button(topframe,height=1,width=9,text="push to test",command=myclick)
buttonTest.grid(row=1,column=2)





mainInterfaceLabel = Label(ip_tracker, text="IP Tracker")




ip_tracker.mainloop()
 