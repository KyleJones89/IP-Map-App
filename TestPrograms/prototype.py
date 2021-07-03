import sqlite3
from tkinter import *
from tksheet import *
from tkinter import filedialog
from sqlite3 import *


#[+] Definitions Pane[+]


#Action for Upload Button
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)


    
#Action for Export Button
def ExportAction(event=None):
    filename = filedialog.asksaveasfilename()
    print('Selected for Import', filename)



#Click Action methods

#checkifEntryEmpty checks to make sure an entry is in the box
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
        liststuff=[]
        print (varentry1.get())
        liststuff.append(varentry1.get())
        liststuff.append(varentry2.get())

        #returnvalue= str(varentry1.get()+" "+str(varentry2.get()))
        
        return liststuff
    else:
        return "This is a bad input"




def putEntryinDB(List):
    conn = sqlite3.connect('IPtrans.db')
    cur = conn.cursor()

    ipaddr=List[0]
    sysnam=List[1]
    cur.execute("INSERT INTO IPsDefined VALUES (\'"+str(ipaddr)+"\',\'"+str(sysnam)+"\','unknown','unknown')")
    conn.commit()
    conn.close()
    selectAllDB()



def selectAllDB():
    print("start")
    for row in cur.execute("SELECT * FROM IPsDefined"):
        
        print(row)
    



def defineDatabase(cursor):
    cursor.execute('''CREATE TABLE IPsDefined
               (IP_Address text, System_Name text,  Date text, Correspondence text)''')




def tableExist(cursor, tablename):
    lst =[]
    lst=cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+tablename+"\"")



def myclick():
    
    putEntryinDB(displayEntryBoxData(ipEntry,nameSpaceEn))


#######################################################################
###########################BLANK FOR SPACING###########################
#######################################################################

conn = sqlite3.connect('IPtrans.db')

cur = conn.cursor()



#defineDatabase(cur)





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

buttonTest = Button(topframe,height=1,width=9,text="push to test",command=myclick)

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
 