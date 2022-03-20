from textwrap import fill
from tkinter import ttk,messagebox
from tkinter import *
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#031F3c",fg="white")
        title.pack(side=TOP,fill=X)

        #=========All variables=======#

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.shift_var=StringVar()
        self.program_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

         #======================Manage frame ======================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3c")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        lbl_roll=Label(Manage_Frame,text="Enrollment",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        txt_Roll.focus()

        lbl_name=Label(Manage_Frame,text="Name",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        lbl_shift=Label(Manage_Frame,text="Shift",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_shift.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        combo_shift=ttk.Combobox(Manage_Frame,textvariable=self.shift_var,font=("times new roman",13,"bold"),state='readonly')
        combo_shift['values']=("--Select--","Frist","Second")
        combo_shift.grid(row=4,column=1,pady=10,padx=10,sticky="w")
        combo_shift.current(0)

        lbl_program=Label(Manage_Frame,text="Program",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_program.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        combo_program=ttk.Combobox(Manage_Frame,textvariable=self.program_var,font=("times new roman",13,"bold"),state='readonly')
        combo_program['values']=("--Select--","Computer","Electronic","Civil","Mechanical")
        combo_program.grid(row=5,column=1,pady=10,padx=10,sticky="w")
        combo_program.current(0)

        lbl_gender=Label(Manage_Frame,text="Gender",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("--Select--","Male","Female","others")
        combo_gender.grid(row=6,column=1,pady=10,padx=10,sticky="w")
        combo_gender.current(0)

        lbl_contact=Label(Manage_Frame,text="Contact",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=7,column=1,pady=10,padx=10,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=8,column=0,pady=10,padx=10,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=8,column=1,pady=10,padx=10,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_address.grid(row=9,column=0,pady=10,padx=10,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=9,column=1,pady=10,padx=10,sticky="w")

        #=================Button frame

        btn_Fame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#031F3c")
        btn_Fame.place(x=15,y=520,width=420)

        Add_btn=Button(btn_Fame,text="Add",width=10,command=self.add_student,activebackground="#031F3c",bg="#08A3D2").grid(row=0,column=0,padx=10,pady=10)

        update_btn=Button(btn_Fame,text="Update",width=10,activebackground="#031F3c",bg="#08A3D2",command=self.update_data).grid(row=0,column=2,padx=10,pady=10)

        delete_btn=Button(btn_Fame,text="Delete",width=10,activebackground="#031F3c",bg="#08A3D2",command=self.delete_data).grid(row=0,column=3,padx=10,pady=10)

        clear_btn=Button(btn_Fame,text="Clear",width=10,activebackground="#031F3c",bg="#08A3D2",command=self.clear).grid(row=0,column=4,padx=10,pady=10)



        #======================Detail frame ======================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3c")
        Detail_Frame.place(x=500,y=100,width=800,height=600)
        
        lbl_search=Label(Detail_Frame,text="Search by",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("--Select--","roll_no","Name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")
        combo_search.current(0)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn=Button(Detail_Frame,text="Search",width=10,pady=5,activebackground="#031F3c",bg="#08A3D2",command=self.search_data).grid(row=0,column=3,padx=10,pady=10)

        show_btn=Button(Detail_Frame,text="Show ALl",width=10,pady=5,activebackground="#031F3c",bg="#08A3D2",command=self.fect_data).grid(row=0,column=4,padx=10,pady=10)

        #============= Table Frame ======================

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#031F3c")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("Enrollment","name","email","shift","program","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Enrollment",text="Enrollment ")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("shift",text="Shift")
        self.student_table.heading("program",text="Program")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Address",text="Address")

        self.student_table['show']='headings'
        self.student_table.column("Enrollment",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("shift",width=100)
        self.student_table.column("program",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fect_data()

    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
           messagebox.showerror("Error","All fields are required!!!!")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.shift_var.get(),
                                                                                    self.program_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.txt_Address.get('1.0', END)
                                                                                    ))

                con.commit()
                self.fect_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been Inserted")
            except Exception as es:
                messagebox.showerror("Erro","Enrollment Already exisit", parent=self.root)


    def fect_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.shift_var.set("")
        self.program_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.shift_var.set(row[3])
        self.program_var.set(row[4])
        self.gender_var.set(row[5])
        self.contact_var.set(row[6])
        self.dob_var.set(row[7])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[8])


    def update_data(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","Please select data!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("update  students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s,shift=%s,program=%s where roll_no=%s",(
                                                                                                                                        self.name_var.get(),
                                                                                                                                        self.email_var.get(),
                                                                                                                                        self.shift_var.get(),
                                                                                                                                        self.program_var.get(),
                                                                                                                                        self.gender_var.get(),
                                                                                                                                        self.contact_var.get(),
                                                                                                                                        self.dob_var.get(),
                                                                                                                                        self.txt_Address.get('1.0', END),
                                                                                                                                        self.Roll_No_var.get()
                                                                                                                                        ))
            con.commit()
            self.fect_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record updated")
    
    def delete_data(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","Please select data!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("delete  from students where roll_no=%s",self.Roll_No_var.get())
            con.commit()
            con.close()
            self.fect_data()
            self.clear()
            messagebox.showinfo("Success", "Record Deleted")

    def search_data(self):
        if self.search_txt.get() ==""  :
            messagebox.showerror("Error","Please Select Identity")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()

            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!= 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                con.commit()
            con.close()        

root=Tk() 
ob=Student(root)
root.mainloop()       
