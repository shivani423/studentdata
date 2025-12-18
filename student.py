import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class std():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
         
        title = tk.Label(self.root, text="Student Record Management System", bd=3, relief="raised",bg="light pink",font=("Elephant",45,"bold"))
        title.pack(side="top",fill="x")

        # Option Frame
        option_frame = tk.Frame(self.root, bd=5, relief="ridge",bg="light yellow",)
        option_frame.place(width=self.width/3, height=self.height-180, x=50, y=100)
        
        # add buttom
        add_btn = tk.Button(option_frame,command=self.addFrameFunc, text="Add_Student", bd=4, relief="raised",bg="Pink",width=20, font=("Arial",20,"bold"))
        add_btn.grid(row=0, column=0, padx=70,pady=30)

        # seach button
        srch_btn = tk.Button(option_frame,command=self.searchFrameFun, text="Search_Student", bd=3, relief="raised",bg="Pink",width=20, font=("Arial",20,"bold"))
        srch_btn.grid(row=1, column=0, padx=30,pady=30)


        # update button
        upd_btn = tk.Button(option_frame,command=self.updateFrameFunc ,text="Update_Student", bd=3, relief="raised",bg="Pink",width=20, font=("Arial",20,"bold"))
        upd_btn.grid(row=2, column=0, padx=30,pady=30)

        # all student button
        all_btn = tk.Button(option_frame,command=self.showAllFrameFunc, text="Show_All", bd=3, relief="raised",bg="Pink",width=20, font=("Arial",20,"bold"))
        all_btn.grid(row=3, column=0, padx=30,pady=30)

        # delete button
        del_btn = tk.Button(option_frame,command=self.removeFrameFunc,text="Remove_Student", bd=3, relief="raised",bg="Pink",width=20, font=("Arial",20,"bold"))
        del_btn.grid(row=4, column=0, padx=30,pady=30)

        # Details Frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge",bg="light yellow")
        self.detFrame.place(width=self.width/2+50, height=self.height-180, x=self.width/3+100, y=100)

        lbl = tk.Label(self.detFrame, text="Recod Details", font=("Arial",30,"bold"),bg="light yellow")
        lbl.pack(side="top",fill="x")
        self.tabFunc()
      # Table Frame
    def tabFunc(self):
        table_frame = tk.Frame(self.detFrame, bd=4,relief="sunken",bg="cyan")
        table_frame.place(width=self.width/2, height=self.height-280, x=23, y=70 )

        # Scrollbar
        x_scroll = tk.Scrollbar(table_frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        y_scroll = tk.Scrollbar(table_frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        # Table
        self.table = ttk.Treeview(table_frame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set,
                                  columns=("roll","name","fname","sub","grade"))
        
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        
        self.table.heading("roll", text="Roll_No")
        self.table.heading("name",text="Name")
        self.table.heading("fname", text="Father_Name")
        self.table.heading("sub",text="Subject")
        self.table.heading("grade",text="Grade")
        self.table["show"] = "headings"
 

        self.table.pack(fill="both", expand=1)


    def addFrameFunc(self):
     self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="light green")
     self.addFrame.place(width=self.width/3, height=self.height-220,
                        x=self.width/3+80, y=100)

     # Roll No
     tk.Label(self.addFrame, text="Roll_No", bg="light green",
             font=("Arial", 15, "bold")).grid(row=0, column=0, padx=20, pady=30)
     self.rollNo = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.rollNo.grid(row=0, column=1, padx=10, pady=30)

    # Name
     tk.Label(self.addFrame, text="Name", bg="light green",
             font=("Arial", 15, "bold")).grid(row=1, column=0, padx=20, pady=30)
     self.name = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.name.grid(row=1, column=1, padx=10, pady=30)

     # Father Name
     tk.Label(self.addFrame, text="Father_Name", bg="light green",
             font=("Arial", 15, "bold")).grid(row=2, column=0, padx=20, pady=30)
     self.fname = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.fname.grid(row=2, column=1, padx=10, pady=30)

     # Subject
     tk.Label(self.addFrame, text="Subject", bg="light green",
             font=("Arial", 15, "bold")).grid(row=3, column=0, padx=20, pady=30)
     self.sub = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.sub.grid(row=3, column=1, padx=10, pady=30)

    # Grade
     tk.Label(self.addFrame, text="Grade", bg="light green",
          font=("Arial", 15, "bold")).grid(row=4, column=0, padx=20, pady=30)
     self.grade = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.grade.grid(row=4, column=1, padx=10, pady=30)

    # Submit Button
     tk.Button(self.addFrame, text="ENTER", command=self.addFunc,
              bd=3, relief="ridge").grid(row=5, column=0, columnspan=2, pady=30)
    
    def desAdd(self):
      try:
          self.addFrame.destroy()
      except:
         pass


  #  add Func
    def addFunc(self):
      rn = self.rollNo.get()
      name = self.name.get()
      fname = self.fname.get()
      sub = self.sub.get()
      grade = self.grade.get()

      if not (rn and name and fname and sub and grade):
        messagebox.showerror("Error", "Please fill all fields!")
        return

      try:
          rNo = int(rn)
      except:
        messagebox.showerror("Error", "Roll number must be numeric!")
        return

      try:
          self.dbFunc()

          self.cur.execute(
            "INSERT INTO student (rollNo, name, fname, sub, grade) VALUES (%s,%s,%s,%s,%s)",
            (rNo, name, fname, sub, grade)
          )
          self.con.commit()

          messagebox.showinfo("Success", f"Student {name} added successfully")

          self.desAdd()

          self.cur.execute("SELECT * FROM student WHERE rollNo=%s", (rNo,))
          row = self.cur.fetchone()

          self.table.delete(*self.table.get_children())
          if row:
            self.table.insert("", tk.END, values=row)

          self.con.close()

      except Exception as e:
          messagebox.showerror("Error", f"Database Error: {e}")
          self.desAdd()
 
  #  serach frame
    def searchFrameFun(self):
          self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="light green")
          self.addFrame.place(width=self.width/3, height=self.height-350,
                        x=self.width/3+80, y=100)

     # Roll No
          optLb1 =  tk.Label(self.addFrame, text="Select: ", bg="light green",font=("Arial", 15, "bold"))
          optLb1 .grid(row=0, column=0, padx=20, pady=25)
          self.option = ttk.Combobox(self.addFrame, width=17, values=("rollNo","name","sub"),font=("arial",15,"bold"))
          self.option.set("Select Option")
          self.option.grid(row=0, column=1, padx=20, pady=25)

 
    # Name
          valLb1 = tk.Label(self.addFrame, text="Value:", bg="light green",font=("Arial", 15, "bold"))
          valLb1.grid(row=1, column=0, padx=20, pady=30)
          self.value = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
          self.value.grid(row=1, column=1, padx=20, pady=25)

 
      
     

    # Submit Button
          okBtn = tk.Button(self.addFrame, text="ENTER", command=self.searchFunc,
              bd=3, relief="ridge")
          okBtn.grid(row=5, column=0, columnspan=2, pady=30)
    

     
     
        
        # serach function
     
    def searchFunc(self):
     opt = self.option.get()
     val = self.value.get()

     if not opt or not val:
        messagebox.showerror("Error", "Please select option and enter value")
        return

     try:
        self.dbFunc()

        # clear table safely
        self.table.delete(*self.table.get_children())

        if opt == "rollNo":
            rn = int(val)
            self.cur.execute(
                "SELECT * FROM student WHERE rollNo=%s",
                (rn,)
            )
            row = self.cur.fetchone()

            if row:
                self.table.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("Info", "No record found")

        else:  # name or sub
            query = f"SELECT * FROM student WHERE {opt}=%s"
            self.cur.execute(query, (val,))
            data = self.cur.fetchall()

            if not data:
                messagebox.showinfo("Info", "No record found")
            else:
                for i in data:
                    self.table.insert("", tk.END, values=i)

        self.con.close()
        self.desAdd()

     except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

    def dbFunc(self):
     self.con = pymysql.connect(
        host="localhost",
        user="root",
        password="SK29@krhps",
        database="mydb"
    )
     
     self.cur = self.con.cursor()

    def updateFrameFunc(self):
     self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="light green")
     self.addFrame.place(
        width=self.width/3,
        height=self.height-220,
        x=self.width/3+80,
        y=100
    )

    # Roll No
     tk.Label(self.addFrame, text="Roll_No", bg="light green",
             font=("Arial", 15, "bold")).grid(row=0, column=0, padx=20, pady=20)
     self.u_roll = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.u_roll.grid(row=0, column=1, padx=10, pady=20)

    # Name
     tk.Label(self.addFrame, text="Name", bg="light green",
             font=("Arial", 15, "bold")).grid(row=1, column=0, padx=20, pady=20)
     self.u_name = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.u_name.grid(row=1, column=1, padx=10, pady=20)

    # Father Name
     tk.Label(self.addFrame, text="Father_Name", bg="light green",
             font=("Arial", 15, "bold")).grid(row=2, column=0, padx=20, pady=20)
     self.u_fname = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.u_fname.grid(row=2, column=1, padx=10, pady=20)

    # Subject
     tk.Label(self.addFrame, text="Subject", bg="light green",
             font=("Arial", 15, "bold")).grid(row=3, column=0, padx=20, pady=20)
     self.u_sub = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.u_sub.grid(row=3, column=1, padx=10, pady=20)

    # Grade
     tk.Label(self.addFrame, text="Grade", bg="light green",
             font=("Arial", 15, "bold")).grid(row=4, column=0, padx=20, pady=20)
     self.u_grade = tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3)
     self.u_grade.grid(row=4, column=1, padx=10, pady=20)

    # Buttons
     tk.Button(
        self.addFrame,
        text="FETCH",
        command=self.fetchUpdateData,
        bd=3, relief="ridge", width=10
    ).grid(row=5, column=0, pady=30)

     tk.Button(
        self.addFrame,
        text="UPDATE",
        command=self.updateFunc,
        bd=3, relief="ridge", width=10
    ).grid(row=5, column=1, pady=30)
     

    def fetchUpdateData(self):
     rn = self.u_roll.get()

     if not rn:
        messagebox.showerror("Error", "Enter Roll Number")
        return
     try:
        self.dbFunc()
        self.cur.execute(
            "SELECT * FROM student WHERE rollNo=%s",
            (int(rn),)
        )
        row = self.cur.fetchone()
        self.con.close()

        if not row:
            messagebox.showerror("Error", "Record not found")
            return

        # clear fields
        self.u_name.delete(0, tk.END)
        self.u_fname.delete(0, tk.END)
        self.u_sub.delete(0, tk.END)
        self.u_grade.delete(0, tk.END)

        # insert data
        self.u_name.insert(0, row[1])
        self.u_fname.insert(0, row[2])
        self.u_sub.insert(0, row[3])
        self.u_grade.insert(0, row[4])
  
     except Exception as e:
         messagebox.showerror("Error", f"{e}")

    def updateFunc(self):
       rn = self.u_roll.get()
       name = self.u_name.get()
       fname = self.u_fname.get()
       sub = self.u_sub.get()
       grade = self.u_grade.get()

       if not (rn and name and fname and sub and grade):
          messagebox.showerror("Error","All filelds are rquired")
          return
       try:
           self.dbFunc()
           self.cur.execute("""
                           UPDATE student
                           SET name=%s, fname=%s, sub=%s, grade=%s
                           WHERE rollNo = %s
                           """,(name,fname ,sub,grade,int(rn)))
          
           self.con.commit()
           self.con.close()

           messagebox.showerror("Success","Record updated successfully")

       except Exception as e:
            messagebox.showerror("Success","Record Updatedd Successfully")

          # refrash table
       try :
         #  clear table
         self.table.delete(*self.table.get_children)
           
         #   database connection
         self.con = pymysql.connect(
            host="localhost",
            user="root",
            password="SK29@krhps",
            database="mydb"
         )
         self.sur = self.con.cursor()

         # correct sql
         self.cur.execute(
            "SELECT * FORM student WHERE rollNo=%s",
            (int(rn),)
         )
         row = self.cur.fetchone()

         if row:
            self.table.insert("",tk.END,values=row)

            self.con.close()
            self.desAdd()

       except Exception as e:
              messagebox.showerror("error",f"{e}")

 
          # Show all button
    def showAllFrameFunc(self):
       self.addFrame = tk.Frame(self.root,bd=5,relief="ridge",bg="light green")
       self.addFrame.place(
          width = self.width/3,
          height=200,
          x=self.width/3+80,
          y=150


       )

       tk.Label(
          self.addFrame,
          text="Show all Student",
          bg="light green",
          font=("Arial",18,"bold")
       ).pack(pady=30)

       tk.Button(
          self.addFrame,
          text="SHOW ALL",
          command=self.showAllFunc,
          bd=3,
          relief="ridge",
          width=15,
          font=("Arial",14,"bold")
       ).pack(pady=20)
             
           
          # show all function

    def showAllFunc(self):
       
       try:
          self.dbFunc()

          self.table.delete(*self.table.get_children())

          self.cur.execute("SELECT*FROM student")
          data = self.cur.fetchall()

          for row in data:
             self.table.insert("",tk.END,values=row)
          self.con.close()
          self.desAdd()
       except Exception as e:
        messagebox.showerror("Error", f"{e}")


    def removeFrameFunc(self):
           self.desAdd()

           self.addFrame = tk.Frame(self.root,bd=5,relief="ridge",bg="light green")
           self.addFrame.place(
              width = self.width/3,
              height=200,
              x=self.width/3+80,
              y=150
           )
           tk.Label(
              self.addFrame,
              text = "Enter Roll Number to Delete",
              bg="light green",
              font =("Arial",16,"bold")

           ).pack(pady=20)

           self.del_roll = tk.Entry(
              self.addFrame,
              width=20,
              font = ("Arial",15,"bold"),
              bd=3
           )
           self.del_roll.pack(pady=10)

           tk.Button ( 
              self.addFrame,
              text="DELETE",
              command=self.removeFunc,
              bg="white",
              fg="red",
              font=("Arial",14,"bold"),
              bd=3,
              relief="ridge",
              width=15
           ).pack(pady=20)
      

      # Remove function
    def removeFunc(self):
       rn = self.del_roll.get()

       if not rn:
          messagebox.showerror("Error","Please enter Roll Number")
          return
       confirm = messagebox.askyesno(
          "Confirm Delete",
          f"Are you sure you want to delete Roll No{rn}?"
       )

       if not confirm:
          return
       
       try:
            self.dbFunc()

          # check record exists
            self.cur.execute("SELECT * FROM student WHERE rollNo=%s",(rn),)
            row = self.cur.fetchone()

            if not row:
             messagebox.showerror("Erro","Record not found")
             self.con.close()
             return
          
         #  Delete record 
            self.cur.execute(
            "DELETE FROM student WHERE rollNo=%s",
            (int(rn),)
           )
            self.con.commit()
            messagebox.showerror("Success","Student deleted successfully")




         # refresh table
            self.table.delete(*self.table.get_children())
            self.cur.execute("SELECT * FROM student")
            data = self.cur.fetchall()

            for i in data:
             self.table.insert("",tk.END,values=i)

             self.con.close()
             self.desAdd()
          
       except Exception as e:
              messagebox.showerror("Error",f"{e}")
             
             
         
          
      


root = tk.Tk()  
obj = std(root)
root.mainloop()  
 
