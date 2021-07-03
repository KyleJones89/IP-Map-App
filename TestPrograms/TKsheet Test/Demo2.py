import tkinter as tk
import datetime as dt
from tkinter import ttk
import sqlite3

def open_window1():
    from tksheet import Sheet
    import tkinter as tk
   

    conn= sqlite3.connect('toko.db')
    c= conn.cursor()

    class demo(tk.Tk):
       def __init__(self):
          tk.Tk.__init__(self)
          self.grid_columnconfigure(0, weight = 1)
          self.grid_rowconfigure(0, weight = 1)
          self.sheet_demo = Sheet(self,
                                  height = 500,
                                  width = 700)
          self.sheet_demo.enable_bindings(("single",
                                   "drag_select",
                                   "column_drag_and_drop",
                                   "column_select",
                                   "row_select",
                                   "arrowkeys",
                                   "column_width_resize",
                                   "row_width_resize",
                                   "copy",
                                   "rc_insert_column",
                                   "rc_insert_row"))

            self.sheet_demo.grid(row = 0, column= 0, sticky= "nswe")
    
            self.headers= ("id","Produk","Stok","Harga Grosir","Harga Eceran")
            self.sheet_demo.headers(self.headers)

            c.execute("SELECT * FROM StokDanHarga")
            h=len(c.fetchall())
            print(h)
            self.data =[[f"Row {r} Column {c}" for c in range(3)] for r in   range(h)]
            self.sheet_demo.data_reference(self.data)
            a=c.execute("SELECT * FROM StokDanHarga")
            j=0
            for row in a:
                # i= len(a)
                r=j   
                print(r,j) 
                self.sheet_demo.set_row_data(r, values = row)   
                j += 1
        


    app= demo()
    app.mainloop()  

root= tk.Tk()
root.title("combobox")
root.geometry("400x400")

buttn = ttk.Button(root, text='STOK DAN HARGA', command=open_window1)
buttn.grid(row=0, column=0)



root.mainloop()