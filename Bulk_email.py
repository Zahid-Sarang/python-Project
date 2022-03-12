from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,filedialog
import pandas as pd
import os
import email_funct 



class BULK_EMAIL:
    def __init__(self,root):
        self.root=root
        self.root.title("BULK EMAIL")
        self.root.geometry("1350x750+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="#031F3c")

#================================================== Frame ======================================#
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=200, y=100, width=900, height=550)

        self.setting_icon=ImageTk.PhotoImage(file="email (2).png")

        btn_setting=Button(frame1,image=self.setting_icon,command=self.setting_window,bg="white",bd=0,activebackground="white",cursor="hand2").place(x=700,y=5)

#=================================================== radio button=================================#

        self.var_choice=StringVar()

        single= Radiobutton(frame1,text="SINGLE",value="SINGLE",variable=self.var_choice,activebackground="white",font=("times new roman",20,"bold"),bg="white",fg="#031F3c",command=self.check_single_or_bulk).place(x=50,y=40)
        Bulk = Radiobutton(frame1, text="BULK",value="BULK",variable=self.var_choice,activebackground="white", font=("times new roman", 20, "bold"), bg="white",fg="#031F3c",command=self.check_single_or_bulk).place(x=250, y=40)
        self.var_choice.set("SINGLE")

#============================================ LABEL & ENTRY FEILDS ===========================================#

        to=Label(frame1,text="To:",font=("times new roman ",15,"bold"),bg="white",fg="#031F3c").place(x=50,y=120)
        subj=Label(frame1,text="SUBJECT",font=("times new roman ",15,"bold"),bg="white",fg="#031F3c").place(x=50,y=170)
        msg=Label(frame1,text="MESSAGE",font=("times new roman ",15,"bold"),bg="white",fg="#031F3c").place(x=50,y=230)

        self.txt_to=Entry(frame1,font=("times new roman",14),bg="light gray")
        self.txt_to.place(x=250,y=120,width=350,height=35)

        self.btn_browse=Button(frame1,text="BROWSE",font=("times new roman",18,"bold"),bg="#031F3c",fg="#08A3D2",activebackground="#08A3D2",activeforeground="#031F3c", cursor="hand2",state=DISABLED,command=self.browse_file)
        self.btn_browse.place(x=610,y=120,width=120,height=30)

        self.txt_sub = Entry(frame1, font=("times new roman", 14), bg="light gray")
        self.txt_sub.place(x=250, y=170, width=480, height=35)

        self.txt_msg =Text(frame1, font=("times new roman", 12), bg="light gray")
        self.txt_msg.place(x=250, y=230, width=480, height=200)

        #=========================STATUS=================================#


        self.lbl_total=Label(frame1,font=("times new roman ",15,"bold"),bg="white",fg="#031F3c")
        self.lbl_total.place(x=50,y=490)

        self.lbl_sent = Label(frame1, font=("times new roman ", 15, "bold"), bg="white", fg="#031F3c")
        self.lbl_sent.place(x=200, y=490)

        self.lbl_left = Label(frame1, font=("times new roman ", 15, "bold"), bg="white", fg="#031F3c")
        self.lbl_left.place(x=320, y=490)

        self.lbl_failed = Label(frame1, font=("times new roman ", 15, "bold"), bg="white", fg="#031F3c")
        self.lbl_failed.place(x=450, y=490)

        self.btn_clear1 = ImageTk.PhotoImage(file="clear.png")
        btn2 = Button(frame1, image=self.btn_clear1, bd=0, cursor="hand2",command=self.clear1).place(x=620, y=490)

        self.btn_save = ImageTk.PhotoImage(file="send.png")
        btn2 = Button(frame1, image=self.btn_save, bd=0, cursor="hand2",command=self.send_email).place(x=750, y=490)

        self.check_file_exist()

    def browse_file(self):
        op=filedialog.askopenfile(initialdir='/',title="Select Excel file for Emails",filetypes=(("All Files","*.*"),("Excel files",".xlsx")))
        if op!=None:
            data=pd.read_excel(op.name)
            if 'email' in data.columns:
                self.emails=list(data['email'])
                c=[]
                for i in self.emails:
                    if pd.isnull(i)==False:
                        c.append(i)
                self.emails=c
                if len(self.emails)>0:
                        self.txt_to.config(state=NORMAL)
                        self.txt_to.delete(0,END)
                        self.txt_to.insert(0, (op.name.split("/")[-1]))
                        self.txt_to.config(state='readonly')
                        self.lbl_total.config(text="Total: "+str(len(self.emails)))
                        self.lbl_sent.config(text="SENT: ")
                        self.lbl_left.config(text="LEFT: ")
                        self.lbl_failed.config(text="FAILED: ")
                else:
                    messagebox.showerror("Error","This file doest have any emails",parent=self.root)
            else:
                messagebox.showerror("Error","please select file which have Email Columns",parent=root)

    def send_email(self):
        x=len(self.txt_msg.get('1.0',END))
        if self.txt_to.get()=="" or self.txt_sub.get()=="" or x==1:
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            if self.var_choice.get()=="SINGLE":
                status=email_funct.email_send_funct(self.txt_to.get(),self.txt_sub.get(),self.txt_msg.get('1.0',END),self.from_,self.pass_)
                if status== "s":
                    messagebox.showinfo("success","EMAIL HAS BEEN SEND",parent=self.root)
                    if status== "f":
                        messagebox.showerror("Error", "EMAIL NOT SENT,TRY Again", parent=self.root)
            if self.var_choice.get() == "BULK":
                self.failed=[]
                self.s_count=0
                self.f_count=0
                for x in self.emails:
                    status = email_funct.email_send_funct(x, self.txt_sub.get(), self.txt_msg.get('1.0', END),self.from_,self.pass_)
                    if status == "s":
                       self.s_count+=1
                    if status == "f":
                       self.f_count_count+=1
                    self.status_bar()
                messagebox.showinfo("success", "EMAIL HAS BEEN SEND,Please Check Staust", parent=self.root)

    def status_bar(self):
        self.lbl_total.config(text="STATUS: " + str(len(self.emails))+"=>>")
        self.lbl_sent.config(text="SENT: "+str(self.s_count))
        self.lbl_left.config(text="LEFT: "+str(len(self.emails)-(self.s_count+self.f_count)))
        self.lbl_failed.config(text="FAILED: "+str(self.f_count))
        self.lbl_total.update()
        self.lbl_sent.update()
        self.lbl_left.update()
        self.lbl_failed.update()

    def check_single_or_bulk(self):
        if self.var_choice.get()=="SINGLE":
            self.btn_browse.config(state=DISABLED)
            self.txt_to.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.clear1()
        if self.var_choice.get() == "BULK":
            self.btn_browse.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.txt_to.config(state='readonly')



    def clear1(self):
        self.txt_to.config(state=NORMAL)
        self.txt_to.delete(0,END)
        self.txt_sub.delete(0,END)
        self.txt_msg.delete('1.0',END)
        self.var_choice.set("SINGLE")
        self.btn_browse.config(state=DISABLED)
        self.lbl_total.config(text="" )
        self.lbl_sent.config(text="")
        self.lbl_left.config(text="")
        self.lbl_failed.config(text="")

#=============================================== CHANGE EMAIL ================================#

    def setting_window(self):
        self.check_file_exist()
        self.root2=Toplevel()
        self.root2.title("Setting")
        self.root2.geometry("700x350+350+90")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="white")
        dis = Label(self.root2,text="Enter the Email address and password from which to send the all emails",font=("Times new roman",16,"bold"), bg="white", fg="#031F3c", ).place(x=0, y=50, relwidth=1)
        from_ = Label(self.root2, text="EMAIL", font=("times new roman ", 15,"bold"), bg="white",fg="#031F3c").place(x=50, y=130)
        pass_ = Label(self.root2, text="PASSWORD", font=("times new roman ", 15,"bold"), bg="white",fg="#031F3c").place(x=50, y=200)

        self.txt_from = Entry(self.root2, font=("times new roman", 14), bg="light gray")
        self.txt_from.place(x=250, y=130, width=330, height=30)

        self.txt_pass = Entry(self.root2, font=("times new roman", 14), bg="light gray",show="*")
        self.txt_pass.place(x=250, y=200, width=330, height=30)

        self.btn_clear2 = ImageTk.PhotoImage(file="clear.png")
        btn2 = Button(self.root2, image=self.btn_clear1, bd=0, cursor="hand2",command=self.clear2).place(x=300, y=260)

        self.btn_save2 = ImageTk.PhotoImage(file="save.png")
        btn2 = Button(self.root2, image=self.btn_save2, bd=0, cursor="hand2",command=self.save_seeting).place(x=430, y=260)
        self.txt_from.insert(0,self.from_)
        self.txt_pass.insert(0,self.pass_)

    def clear2(self):
        self.txt_from.delete(0,END)
        self.txt_pass.delete(0,END)

    def check_file_exist(self):
        if  os.path.exists("EMAIL DATA.txt")==False:
            f = open('EMAIL DATA.txt', 'w')
            f.write ("," )
            f.close()
        f2=open('EMAIL DATA.txt','r')
        self.credentials=[]
        for i in f2:
            self.credentials.append([i.split(",")[0],i.split(",")[1]])
            self.from_=self.credentials[0][0]
            self.pass_ = self.credentials[0][1]


    def save_seeting(self):
        if self.txt_from.get()=="" or self.txt_pass.get()=="":
            messagebox.showinfo("Error","All fields are required",parent=self.root2)
        else:
            f=open('EMAIL DATA.txt','w')
            f.write(self.txt_from.get()+","+self.txt_pass.get())
            f.close()
            messagebox.showinfo("Success","SAVED SUCCESSFULLY",parent=self.root2)
            self.check_file_exist()


root=Tk()
obj=BULK_EMAIL(root)
root.mainloop()