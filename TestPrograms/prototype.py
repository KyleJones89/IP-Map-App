from tkinter import *
from tksheet import *
from tkinter import filedialog


#[+] Definitions Pane[+]



def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def ExportAction(event=None):
    filename = filedialog.asksaveasfilename()
    print('Selected for Import', filename)

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


#def myclick():
    #
    #mylabel = Label(topframe, text=displayEntryBoxData(ipEntry,nameSpaceEn))
    #
    #mylabel.grid(row=2,column=2)


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

bottomFrame=Frame(ip_tracker,width=600,height=50,pady=3).grid(row=4, column= 0,rowspan=6,columnspan=9)

#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################



#[+] Initialize Widgets[+]
uploadButton =  Button(topframe,text= "Import Data", command=UploadAction)

exportButton =  Button(topframe,text= "Export Data",command=ExportAction)

ipLabel = Label(topframe,text="Enter IP Address: ")

ipEntry = Entry(topframe, width = 50, borderwidth = 5)

nameSpaceLabel = Label(topframe, text="Enter Name of System: ")

nameSpaceEn = Entry(topframe, width = 50, borderwidth = 5)

buttonTest = Button(topframe,height=1,width=9,text="push to test")#,command=myclick)

mainInterfaceLabel = Label(ip_tracker, text="IP Tracker")

dataSheet = Sheet(bottomFrame,total_columns=4,total_rows=16)

dataSheet.set_sheet_data()

dataSheet.enable_bindings(("single_select", "row_select","column_width_resize","arrowkeys","right_click_popup_menu",
"rc_select","rc_insert_row","rc_delete_row", "copy","cut","paste","delete","undo","edit_cell"))

#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################


#{+}Place Widgets{+}
uploadButton.grid(row=0, column=0)
exportButton.grid(row=0,column=1)
ipLabel.grid(row = 0,column = 5)
ipEntry.grid(row = 0, column = 6)
nameSpaceLabel.grid(row = 0,column = 7)
nameSpaceEn.grid(row = 0, column = 8)
buttonTest.grid(row=1,column=7)
dataSheet.grid(row=4,column=0,columnspan=9,sticky='ew')






#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################



#{+}END OF PROGRAM. INITIATE LOOP{+}
ip_tracker.mainloop()
#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################
 