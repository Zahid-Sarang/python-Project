from tkinter import *
from tkinter import ttk,messagebox
import pymysql
import pandas.io.sql as sql
import xlwt


window=Tk()
window.title("Data Insert")
window.config(bg="#08A3D2")

#=========All variables=======#

Roll_No_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var=StringVar()
shift_var=StringVar()
program_var=StringVar()
search_by=StringVar()
search_txt=StringVar()

def send():
    window.destroy()
    import Bulk_email

def import_execl():
    con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
    cur = con.cursor()
    df = sql.read_sql('select * from student', con)
    df.to_excel('student.xls')



def fetch_data():
    con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)
        con.commit()
    con.close()


def add_student():
    if Roll_No_var.get()=="" or name_var.get()=="":
        messagebox.showerror("Error","All fields are required!!!!")
    else:
        try:
          con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
          cur = con.cursor()
          cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Roll_No_var.get(),
                                                                               name_var.get(),
                                                                               email_var.get(),
                                                                               shift_var.get(),
                                                                               program_var.get(),
                                                                               gender_var.get(),
                                                                               contact_var.get(),
                                                                               dob_var.get(),
                                                                               txt_Address.get('1.0', END)
                                                                               ))

          con.commit()
          fetch_data()
          clear()
          import_execl()
          con.close()
          messagebox.showinfo("Success","Record has been Inserted")
        except Exception as es:
            messagebox.showerror("Erro","Enrollment Already exisit", parent=window)


def clear():
    Roll_No_var.set("")
    name_var.set("")
    email_var.set("")
    shift_var.set("")
    program_var.set("")
    gender_var.set("")
    contact_var.set("")
    dob_var.set("")
    txt_Address.delete("1.0",END)

def get_cursor(ev):
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content['values']
    Roll_No_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    shift_var.set(row[3])
    program_var.set(row[4])
    gender_var.set(row[5])
    contact_var.set(row[6])
    dob_var.set(row[7])
    txt_Address.delete("1.0",END)
    txt_Address.insert(END,row[8])

def update_data():
    if Roll_No_var.get()=="" or name_var.get()=="":
        messagebox.showerror("Error","Please select data!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
        cur = con.cursor()
        cur.execute("update  student set name=%s,email=%s,shift=%s,program=%s,gender=%s,contact=%s,dob=%s,address=%s where Enroll_no=%s",(
                                                                               name_var.get(),
                                                                               email_var.get(),
                                                                               shift_var.get(),
                                                                               program_var.get(),
                                                                               gender_var.get(),
                                                                               contact_var.get(),
                                                                               dob_var.get(),
                                                                               txt_Address.get('1.0', END),
                                                                               Roll_No_var.get()
                                                                               ))
        con.commit()
        fetch_data()
        clear()
        con.close()
        messagebox.showinfo("Success","Record updated")

def delete_data():
    if Roll_No_var.get()=="" or name_var.get()=="":
        messagebox.showerror("Error","Please select data!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
        cur = con.cursor()
        cur.execute("delete  from student where Enroll_no=%s",Roll_No_var.get())
        con.commit()
        con.close()
        fetch_data()
        clear()
        messagebox.showinfo("Success", "Record Deleted")


def search_data():
    if search_txt.get() ==""  :
        messagebox.showerror("Error","Please Select Identity")
    else:
        con = pymysql.connect(host="localhost", user="root", password="Sarang@123", database="attendance")
        cur = con.cursor()

        cur.execute("select * from student where "+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!= 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('',END,values=row)
            con.commit()
        con.close()


#======================Manage frame

Manage_Frame=Frame(window,bd=4,relief=RIDGE,bg="#031F3c")
Manage_Frame.place(x=10,y=30,width=450,height=630)

lbl_roll=Label(Manage_Frame,text="Enrollment",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

txt_Roll=Entry(Manage_Frame,textvariable=Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")
txt_Roll.focus()

lbl_name=Label(Manage_Frame,text="Name",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

txt_name=Entry(Manage_Frame,textvariable=name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")

lbl_Email=Label(Manage_Frame,text="Email",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_Email.grid(row=3,column=0,pady=10,padx=10,sticky="w")

txt_Email=Entry(Manage_Frame,textvariable=email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_Email.grid(row=3,column=1,pady=10,padx=10,sticky="w")

lbl_shift=Label(Manage_Frame,text="Shift",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_shift.grid(row=4,column=0,pady=10,padx=10,sticky="w")

combo_shift=ttk.Combobox(Manage_Frame,textvariable=shift_var,font=("times new roman",13,"bold"),state='readonly')
combo_shift['values']=("--Select--","Frist","Second")
combo_shift.grid(row=4,column=1,pady=10,padx=10,sticky="w")
combo_shift.current(0)

lbl_program=Label(Manage_Frame,text="Program",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_program.grid(row=5,column=0,pady=10,padx=10,sticky="w")

combo_program=ttk.Combobox(Manage_Frame,textvariable=program_var,font=("times new roman",13,"bold"),state='readonly')
combo_program['values']=("--Select--","Computer","Electronic","Civil","Mechanical")
combo_program.grid(row=5,column=1,pady=10,padx=10,sticky="w")
combo_program.current(0)

lbl_gender=Label(Manage_Frame,text="Gender",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_gender.grid(row=6,column=0,pady=10,padx=10,sticky="w")

combo_gender=ttk.Combobox(Manage_Frame,textvariable=gender_var,font=("times new roman",13,"bold"),state='readonly')
combo_gender['values']=("--Select--","Male","Female","others")
combo_gender.grid(row=6,column=1,pady=10,padx=10,sticky="w")
combo_gender.current(0)



lbl_contact=Label(Manage_Frame,text="Contact",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_contact.grid(row=7,column=0,pady=10,padx=10,sticky="w")

txt_contact=Entry(Manage_Frame,textvariable=contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_contact.grid(row=7,column=1,pady=10,padx=10,sticky="w")

lbl_dob=Label(Manage_Frame,text="D.O.B",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_dob.grid(row=8,column=0,pady=10,padx=10,sticky="w")

txt_dob=Entry(Manage_Frame,textvariable=dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_dob.grid(row=8,column=1,pady=10,padx=10,sticky="w")

lbl_address=Label(Manage_Frame,text="Address",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_address.grid(row=9,column=0,pady=10,padx=10,sticky="w")

txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
txt_Address.grid(row=9,column=1,pady=10,padx=10,sticky="w")

send_btn=Button(Manage_Frame,text="Send Email",width=10,command=send,activebackground="#031F3c",bg="#08A3D2").grid(row=15,column=0,padx=10,pady=10,sticky="w")

#=================Button frame

btn_Fame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#031F3c")
btn_Fame.place(x=15,y=550,width=420)

Add_btn=Button(btn_Fame,text="Add",width=10,command= add_student,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=0,padx=10,pady=10)

update_btn=Button(btn_Fame,text="Update",width=10,activebackground="#031F3c",bg="#08A3D2",command=update_data).grid(row=0,column=2,padx=10,pady=10)

delete_btn=Button(btn_Fame,text="Delete",width=10,command=delete_data,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=3,padx=10,pady=10)

clear_btn=Button(btn_Fame,text="Clear",width=10,command=clear,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=4,padx=10,pady=10)


#======================Detail frame

Detail_Frame=Frame(window,bd=4,relief=RIDGE,bg="#031F3c")
Detail_Frame.place(x=490,y=30,width=800,height=630)

lbl_search=Label(Detail_Frame,text="Search by",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

combo_search=ttk.Combobox(Detail_Frame,textvariable=search_by,width=15,font=("times new roman",13,"bold"),state='readonly')
combo_search['values']=("--Select--","Enroll_no","Name","Contact")
combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
combo_search.current(0)

txt_search=Entry(Detail_Frame,textvariable=search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

search_btn=Button(Detail_Frame,text="Search",width=10,pady=5,command=search_data,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=3,padx=10,pady=10)

show_btn=Button(Detail_Frame,text="Show ALl",width=10,pady=5,command=fetch_data,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=4,padx=10,pady=10)


#============= Table Frame

Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#031F3c")
Table_Frame.place(x=10,y=70,width=760,height=500)

scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
student_table=ttk.Treeview(Table_Frame,columns=("Enrollment","name","email","shift","program","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("Enrollment",text="Enrollment NO")
student_table.heading("name",text="Name")
student_table.heading("email",text="Email")
student_table.heading("shift",text="Shift")
student_table.heading("program",text="Program")
student_table.heading("gender",text="Gender")
student_table.heading("contact",text="Contact")
student_table.heading("dob",text="D.O.B")
student_table.heading("Address",text="Address")

student_table['show']='headings'
student_table.column("Enrollment",width=100)
student_table.column("name",width=100)
student_table.column("email",width=100)
student_table.column("shift",width=100)
student_table.column("program",width=100)
student_table.column("gender",width=100)
student_table.column("contact",width=100)
student_table.column("dob",width=100)
student_table.column("Address",width=150)
student_table.pack(fill=BOTH,expand=1)
student_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()

window.geometry("1400x800+0+0")
window.mainloop()