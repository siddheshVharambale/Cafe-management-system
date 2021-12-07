from tkinter import *
from typing import ValuesView

from PIL import ImageTk

from tkinter import messagebox

import pymysql

from cryptography.fernet import Fernet

class Login:

   def __init__(self,root):

      self.root=root
      
            
      self.root.resizable(True,True)

      self.loginform()

   def loginform(self):
      self.root.geometry("1550x1300+0+0")

      self.root.title("SDS Cafe")

      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=1000,width=1550)

     

      self.img=ImageTk.PhotoImage(file="bg.jpg")

      img=Label(Frame_login,image=self.img).place(x=0,y=0)

      

      frame_input=Frame(self.root,bg='white')

      frame_input.place(x=280,y=150,height=470,width=370)



      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')

      label1.place(x=75,y=20)



      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.username_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

      self.username_txt.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',show='*')

      self.password.place(x=30,y=245,width=270,height=35)


      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)

     



   def login(self):

      if self.username_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='sid18@', database="SDS")

            cur=con.cursor()
            cur.execute('select * from register where username=%s and passw=%s',(self.username_txt.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username Or Password',parent=self.root)

               self.loginclear()

               
            else:

               self.appscreen()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

            

   def Register(self):

      self.root.geometry("1550x1300+0+0")
      self.root.title("Registration system for Apps")

      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=1010,width=1550)

      

      self.img=ImageTk.PhotoImage(file="mug.jpg")

      img=Label(Frame_login1,image=self.img).place(x=0,y=0)

      

      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=100,y=200,height=470,width=630)



      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')

      label1.place(x=160,y=20)



      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',show='*')

      self.entry2.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

      self.entry3.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="Confirm Password",

      font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',show='*')

      self.entry4.place(x=330,y=245,width=270,height=35)



      btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

      text="Already Registered?Login",cursor="hand2",

      font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)





   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="sid18@")

            cur=con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS SDS")
            cur.execute("USE SDS")
            cur.execute("CREATE TABLE IF NOT EXISTS register(username text,email text,passw varchar(15),confpass varchar(15))")
            
            cur.execute("select * from register where email=%s",self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email" ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull",parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)



   def appscreen(self):

   
      self.root.geometry("1400x720+60+40")
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1500)
      '''con=pymysql.connect(host="localhost",user="root", passwd= "S403ad248",database="SDS")
      cur=con.cursor()

      cur.execute("CREATE TABLE IF NOT EXISTS menu(foodid text,name text,price numeric, qt numeric)")'''

      self.img_bg1=ImageTk.PhotoImage(file="bg-1.jpg")

      img=Label(Frame_login,image=self.img_bg1).place(x=0,y=0)

      label1=Label(Frame_login,text=" Welcome SDS Cafe",font=('times new roman',32,'bold'),fg="black")
      label1.place(x=500,y=0)

      self.img=ImageTk.PhotoImage(file="1.jpg")
      img=Label(Frame_login,image=self.img).place(x=10,y=70)

      self.img1=ImageTk.PhotoImage(file="2_pizza.jpg")
      img1=Label(Frame_login,image=self.img1).place(x=360,y=70)

      self.img2=ImageTk.PhotoImage(file="cofe.jpg")

      img2=Label(Frame_login,image=self.img2).place(x=715,y=70)

      self.img3=ImageTk.PhotoImage(file="momo-1.jpg")

      img3=Label(Frame_login,image=self.img3).place(x=1070,y=70)

      self.img4=ImageTk.PhotoImage(file="1-fries.jpg")

      img4=Label(Frame_login,image=self.img4).place(x=10,y=370)

      self.img5=ImageTk.PhotoImage(file="1-sand.jpg")

      img5=Label(Frame_login,image=self.img5).place(x=360,y=370)

      self.img6=ImageTk.PhotoImage(file="nacho.jpg")

      img6=Label(Frame_login,image=self.img6).place(x=715,y=370)

      self.img7=ImageTk.PhotoImage(file="samo.jpg")

      img7=Label(Frame_login,image=self.img7).place(x=1070,y=370)

   #------------------Labels and Entries-------------------------------------
      sandwich=IntVar()
      pizza=IntVar()
      coffee=IntVar()
      momo=IntVar()
      fries=IntVar()
      gril=IntVar()
      pasta=IntVar()
      samosa=IntVar() 
   
      l1=Label(Frame_login,text="Rs.70",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l1.place(x=20,y=280)

      self.e1=Entry(Frame_login,textvariable=sandwich,font=("times new roman",13,"bold"),bg='lightgray')
      self.e1.place(x=100,y=280,width=150,height=30)

      l2=Label(Frame_login,text="Rs.99",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l2.place(x=360,y=280)

      self.e2=Entry(Frame_login,textvariable=pizza,font=("times new roman",13,"bold"),bg='lightgray')
      self.e2.place(x=440,y=280,width=150,height=30)

      l3=Label(Frame_login,text="Rs.40",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l3.place(x=720,y=280)

      self.e3=Entry(Frame_login,textvariable= coffee,font=("times new roman",13,"bold"),bg='lightgray')
      self.e3.place(x=800,y=280,width=150,height=30)

      l4=Label(Frame_login,text="Rs.60",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l4.place(x=1080,y=280)

      self.e4=Entry(Frame_login,textvariable=momo,font=("times new roman",13,"bold"),bg='lightgray')
      self.e4.place(x=1160,y=280,width=150,height=30)

      l5=Label(Frame_login,text="Rs.50",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l5.place(x=20,y=590)

      self.e5=Entry(Frame_login,textvariable=fries,font=("times new roman",13,"bold"),bg='lightgray')
      self.e5.place(x=100,y=590,width=150,height=30)

      l6=Label(Frame_login,text="Rs.90",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l6.place(x=360,y=590)

      self.e6=Entry(Frame_login,textvariable=gril,font=("times new roman",13,"bold"),bg='lightgray')
      self.e6.place(x=440,y=590,width=150,height=30)

      l7=Label(Frame_login,text="Rs.75",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l7.place(x=730,y=590)

      self.e7=Entry(Frame_login,textvariable=pasta,font=("times new roman",13,"bold"),bg='lightgray')
      self.e7.place(x=800,y=590,width=150,height=30)

      l8=Label(Frame_login,text="Rs.60",font=('times new roman',15,'bold'),fg="black",bg="light grey")
      l8.place(x=1080,y=590)

      self.e8=Entry(Frame_login,textvariable=samosa,font=("times new roman",13,"bold"),bg='lightgray')
      self.e8.place(x=1160,y=590,width=150,height=30)

      

   #logout button
      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="blue",bd=0,width=15,height=1)

      btn2.place(x=1200,y=10)

   #bill button

      btn3=Button(Frame_login,text="Bill",cursor="hand2",command =self.total,font=("times new roman",15),fg="white",bg="Orange",bd=0,width=15,height=1)

      btn3.place(x=600,y=660)
   
   #delete button
      btn3=Button(Frame_login,text="Delete",cursor="hand2",command =self.delete,font=("times new roman",10),fg="white",bg="red",bd=0,width=8,height=1)

      btn3.place(x=2,y=9)
   #update button
      btn3=Button(Frame_login,text="Update",cursor="hand2",command =self.update,font=("times new roman",10),fg="black",bg="yellow",bd=0,width=8,height=1)

      btn3.place(x=100,y=9)
   
   def delete(self):
        self.root.geometry("400x400+300+60")
        Frame_login2=Frame(self.root,bg="light grey")
        Frame_login2.place(x=0,y=0,height=400,width=400)
        self.root.resizable(False,False)
        
        self.img=ImageTk.PhotoImage(file="dele.png")

        img=Label(Frame_login2,image=self.img).place(x=0,y=0)
         

        con = pymysql.connect(host="localhost",user="root",password="sid18@",database='SDS')
        cur=con.cursor()
        cur.execute("DELETE FROM register WHERE username=%s",(self.username_txt.get(),))
        con.commit()
        con.close()

        #logout button
        btn_1=Button(Frame_login2,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",10),fg="white",bg="blue",bd=0,width=5,height=1)
        btn_1.place(x=360,y=2)

   def update(self):
         self.root.geometry("600x600+500+80")
         Frame_login1=Frame(self.root,bg="white")
         Frame_login1.place(x=0,y=0,height=600,width=600)
         self.root.resizable(False,False)

         self.password=StringVar()
         self.confrmpass=StringVar()

         label4=Label(Frame_login1,text="Update Password ",font=("Goudy old style",30,"bold"),fg='orangered',bg='white')

         label4.place(x=200,y=20)

         label4=Label(Frame_login1,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

         label4.place(x=260,y=95)

         self.entry1=Entry(Frame_login1,font=("times new roman",15,"bold"),bg='lightgray')

         self.entry1.place(x=200,y=145,width=270,height=35)

         label5=Label(Frame_login1,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

         label5.place(x=260,y=255)

         self.entry2=Entry(Frame_login1,font=("times new roman",15,"bold"),bg='lightgray')

         self.entry2.place(x=200,y=305,width=270,height=35)

         #update button
         btn2=Button(Frame_login1,text="Update",command=self.updatedb(password='',confrmpass='',username_txt=''),cursor="hand2",font=("times new roman",10),fg="white",bg="blue",bd=0,width=5,height=1)
         btn2.place(x=300,y=500)

         if self.entry1.get()!=self.entry2.get():

           messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

        
         self.password=self.entry1.get()
         self.confrmpass=self.entry2.get()

   def updatedb(password='',confrmpass='',username_txt=''):
               con = pymysql.connect(host="localhost",user="root",password="sid18@",database='SDS')
               cur=con.cursor()
               cur.execute("UPDATE register SET passw=%s , confpass=%s  WHERE username=%s",(password,confrmpass,username_txt))
               con.commit()

               messagebox.showinfo("","Password and Confirm Password Updated successfully")
               con.close()

     



   def total(self):
         self.root.geometry("400x400+300+60")
         Frame_login1=Frame(self.root,bg="white")
         Frame_login1.place(x=0,y=0,height=400,width=400)
         self.root.resizable(False,False)

         self.img=ImageTk.PhotoImage(file="order.jpg")

         img=Label(Frame_login1,image=self.img).place(x=0,y=0)

         self.sandwich=self.e1.get()
         self.pizza=self.e2.get()
         self.coffee=self.e3.get()
         self.momo=self.e4.get()
         self.fries=self.e5.get()
         self.gril=self.e6.get()
         self.pasta=self.e7.get()
         self.samosa=self.e8.get()

         total1=IntVar()
         total1=((int(self.sandwich)*70) + (int(self.pizza)*99) + (int(self.coffee)*40) +(int(self.momo)*60) + (int(self.fries)*50) +(int(self.gril)*90) +(int(self.pasta)*75) + (int(self.samosa)*60))
         
         labelb=Label(Frame_login1,text=("Total Amount : ",total1),font=('times new roman',15,'bold'),fg="black",bg='gray')
         labelb.place(x=120,y=40)
         labeln=Label(Frame_login1,text="Thank you for placing order\n surely visit next time too 😊😇!!",font=('times new roman',15,'bold'),fg="black",bg="light grey")
         labeln.place(x=70,y=340)
         
         #logout button
         btn2=Button(Frame_login1,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",10),fg="white",bg="blue",bd=0,width=5,height=1)
         btn2.place(x=360,y=2)


   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)



   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)



root=Tk()

ob=Login(root)

root.mainloop()