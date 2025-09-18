from tkinter import *
from tkinter import messagebox
import time
import my_db
#==props====================================================================================================================================
mainwin = Tk()
mainwin.geometry('600x500+400+200')
mainwin.resizable(0,0)
mainwin.title('Login Form')
mainwin.config(bg= "#222222")

db1 = my_db.Data_base('D:/dbfiles/mydata01.db')
#==functions================================================================================================================================
def add():
    fname = ent_fname.get().strip().title()
    lname = ent_lname.get().strip().title()
    code_meli = ent_code_meli.get().strip()
    score = ent_score.get().strip()
    if fname == '' or lname == '' or code_meli == '' or score == '':
         messagebox.showerror('ERROR','Please fill all the fields')
         return
    
    if not code_meli.isdigit():
        messagebox.showerror('ERROR','Code meli most be number') 

    if len(code_meli) != 10:
        messagebox.showerror('ERROR','Code meli most be 10 numbers')
        return
    
    if not score.isdigit():
        messagebox.showerror('ERROR','Score must be number')
        return
    
    if score > '20.0':
        messagebox.showerror('ERROR','Enter the Correct Score')
        return
    
    db1.insert(fname,lname,code_meli,score)
    messagebox.showinfo('INFO','Record Inserted Succesfully!')
    clear()
#===========================================================================================================================================
all_records = []
#__Show_____________________________________________________________________________________________________________________________________
def show():
    lstbox.delete(0,END)
    records = db1.select()
    for rec in records:
        all_records.append(rec)
        display_text = ', '.join(str(item) for item in rec)
        lstbox.insert(END, display_text)
#__Delete___________________________________________________________________________________________________________________________________
def Del():
    index = lstbox.curselection()
    if not index:
        messagebox.showwarning('Warning','Please choose one of the list first!')
        return   
    
    record = lstbox.get(index)
  
    dell = messagebox.askyesno('INFO',"Are You Sure To Delete?")
    if dell:
        db1.delete(record[0])
        clear()
        show()
#__Select_items_____________________________________________________________________________________________________________________________
def select_items(event):
    clear()
    index = lstbox.curselection()
    if not index:
        return
    
    record = all_records[index[0]] 
    ent_fname.delete(0, END)
    ent_fname.insert(0, record[1])
    ent_lname.delete(0, END)
    ent_lname.insert(0, record[2])
    ent_code_meli.delete(0, END)
    ent_code_meli.insert(0, record[3])
    ent_score.delete(0, END)
    ent_score.insert(0, record[4])
#__Clear____________________________________________________________________________________________________________________________________
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_code_meli.delete(0,END)
    ent_score.delete(0,END)
    ent_fname.focus()
#__update___________________________________________________________________________________________________________________________________
def update_record():
    index = lstbox.curselection()
    score = ent_score.get()
    if not index:
        messagebox.showwarning('Warning','Please choose one of the list first!')
        return   
    
    record = lstbox.get(index)
    db1.update(record[0],ent_fname.get(),ent_lname.get()
               ,ent_code_meli.get(),ent_score.get())
    messagebox.showinfo('UPDATE','Record updated Succesfully!')
    show()
    clear()
#__Exit_____________________________________________________________________________________________________________________________________
def exit():
    exitt = messagebox.askyesno('EXIT',"Do You Want to Exit?")
    if exitt:
        time.sleep(0.5)
        mainwin.destroy()
#==widgets==================================================================================================================================
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  
#==labels===================================================================================================================================
lbl_fname = Label(text= 'Fname',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA")
lbl_fname.place(x= 10,y= 15)

lbl_lname = Label(text= 'Lname',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA")
lbl_lname.place(x= 345,y= 15)

lbl_code_meli = Label(text= 'Code Meli',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA")
lbl_code_meli.place(x= 10,y= 45)

lbl_score = Label(text= 'Score',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA")
lbl_score.place(x= 10,y= 75)

lbl_star1 = Label(text= '*',font= ("times new roman", 16,'bold'),bg= "#222222",fg="#7C6800")
lbl_star1.place(x= 110,y= 17)

lbl_star2 = Label(text= '*',font= ("times new roman", 16,'bold'),bg= "#222222",fg="#7C6800")
lbl_star2.place(x= 410,y= 17)

lbl_star3 = Label(text= '*',font= ("times new roman", 16,'bold'),bg= "#222222",fg="#7C6800")
lbl_star3.place(x= 110,y= 47)
#==entrise==================================================================================================================================
ent_fname = Entry(font= ("times new roman", 10,'bold'),bg= '#AAAAAA',fg= '#222222')
ent_fname.place(x= 130 ,y= 18)

ent_lname = Entry(font= ("times new roman", 10,'bold'),bg= '#AAAAAA',fg= '#222222')
ent_lname.place(x= 430 ,y= 18)

ent_code_meli = Entry(font= ("times new roman", 10,'bold'),bg= '#AAAAAA',fg= '#222222')
ent_code_meli.place(x= 130 ,y= 48)

ent_score = Entry(font= ("times new roman", 10,'bold'),bg= '#AAAAAA',fg= '#222222')
ent_score.place(x= 130 ,y= 78)
#==buttons==================================================================================================================================
btn_add = Button(text= 'Add',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA",command= add)
btn_add.place(x= 15,y= 150, width= 100)

btn_clear = Button(text= 'Clear',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA",command= clear)
btn_clear.place(x= 15,y= 205, width= 100)

btn_delete = Button(text= 'Delete',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA",command= Del)
btn_delete.place(x= 15,y= 255, width= 100)

btn_select = Button(text= 'Update',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA",command= update_record)
btn_select.place(x= 15,y= 310, width= 100)

btn_update = Button(text= 'Select',font= ("times new roman", 14,'bold'),bg= "#222222",fg="#AAAAAA",command= show)
btn_update.place(x= 15,y= 365, width= 100)

btn_exit = Button(text= 'Exit',font= ("times new roman", 12,'bold'),bg= "#222222",fg="#AAAAAA",command= exit)
btn_exit.place(x= 15,y= 460, width= 564)
#==scrollbar================================================================================================================================
scrllbar_y = Scrollbar(mainwin, orient= VERTICAL)
scrllbar_y.place(x= 575,y= 145, height= 260,width=15)

scrllbar_x = Scrollbar(mainwin,orient= HORIZONTAL)
scrllbar_x.place(x= 145,y= 402, width= 430)
#==listbox==================================================================================================================================
lstbox = Listbox(mainwin,font= ("times new roman", 14,'bold'),bg="#AAAAAA",fg= "#222222"
                 ,yscrollcommand= scrllbar_y.set,
                 xscrollcommand= scrllbar_x.set)
lstbox.place(x= 145,y= 145, width= 430,height= 260)

lstbox.bind('<<ListboxSelect>>',select_items)

scrllbar_y.config(command= lstbox.yview)

scrllbar_x.config(command= lstbox.xview)
#==TheEnd===================================================================================================================================
mainwin.mainloop()