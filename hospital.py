from telnetlib import DET
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter import font
import tkinter
from turtle import width
# from certifi import contents
import mysql.connector
from numpy import insert

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose = StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate = StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.Dose = StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StoragrAdvice = StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress = StringVar()


        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",bg="white",font=("times new roman",50,"bold",))
        lbltitle.pack(side=TOP,fill=X)

        #=============================DataFrame========================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",12,"bold"),
        text="Patient Infromation"
        )

        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",12,"bold"),
        text="Prescription"
        )

        DataFrameRight.place(x=990,y=5,width=460,height=350)
        
        #==================== Buttons Frame ============

        Buttonframe=Frame(
            self.root,bd=20,relief=RIDGE
        )

        Buttonframe.place(x=0,y=530,width=1530,height=70)
        #============================= Details Frame =====================
        Detailsframe=Frame(
            self.root,bd=20,relief=RIDGE
        )

        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # DATAFRAME LEFT
        lblNameTablet=Label(DataFrameLeft, font=("arial",12,"bold"), text="Name of Tablet")
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),
        width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Dolo 650","Acetaminophen","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.ref,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTable=Label(DataFrameLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOfTable.grid(row=3,column=0,sticky=W)
        txtNoOfTable=Entry(DataFrameLeft,textvariable=self.NumberofTablets,font=("arial",13,"bold"),width=35)
        txtNoOfTable.grid(row=3,column=1) 
        
        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1) 

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,textvariable=self.IssueDate,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.ExpDate,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,textvariable=self.DailyDose,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Infomation:",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,textvariable=self.FurtherInformation,font=("arial",13,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,textvariable=self.DrivingUsingMachine,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,textvariable=self.StoragrAdvice,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,textvariable=self.HowToUseMedication,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,textvariable=self.PatientId,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,textvariable=self.nhsNumber,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataFrameLeft,textvariable=self.PatientName,font=("arial",13,"bold"),width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,textvariable=self.DateOfBirth,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAdress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAdress.grid(row=8,column=2,sticky=W)
        txtPatientAdress=Entry(DataFrameLeft,textvariable=self.PatientAddress,font=("arial",13,"bold"),width=35)
        txtPatientAdress.grid(row=8,column=3)

        #===================== DataFrameRight =======================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #======================== Buttons ==============
        btnPrescription = Button(Buttonframe,text="Prescription",command=lambda: self.Prescription(),fg="white",bg="green",font=("Arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,text="Prescription Data",fg="white",bg="green",font=("Arial",12,"bold"),command=lambda: self.iPrescription(),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(Buttonframe,text="Update",command=self.update_data,fg="white",bg="green",font=("Arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe,command=self.idelete,text="Delete",fg="white",bg="green",font=("Arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe,command=self.Clear,text="Clear",fg="white",bg="green",font=("Arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit = Button(Buttonframe,command=self.iExit,text="Exit",fg="white",bg="green",font=("Arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #============================== Table ==============================
        #==============================Scroll Bar ==========================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameOftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameOftable",text="Name Of the table")
        self.hospital_table.heading("ref",text="Refernce No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        

        self.hospital_table.column("nameOftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        #======================================= Functionality Declartion ======================
    
    def iPrescription(self):

        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="amaan",database="hospital")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StoragrAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","All data has been inserted")    

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost",username="root",password="amaan",database="hospital")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()  

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StoragrAdvice.set(row[8])
        self.nhsNumber.set(row[9]) 
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        

    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="amaan",database="hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where ReferenceNo=%s",(
                            self.Nameoftablets.get(),
                            self.Dose.get(),
                            self.NumberofTablets.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpDate.get(),
                            self.DailyDose.get(),
                            self.StoragrAdvice.get(),
                            self.nhsNumber.get(),
                            self.PatientName.get(),
                            self.DateOfBirth.get(),
                            self.PatientAddress.get(),
                            self.ref.get(),
                        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","data has been updated")
        self.fetch_data()

    
    def Prescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StoragrAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivinfUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateofBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")


    def idelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="amaan",database="hospital")
        my_cursor = conn.cursor()
        query = "delete from hospital where ReferenceNo=%s"
        value=([self.ref.get()])
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
        self.fetch_data()

    
    def Clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.Dose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StoragrAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
 
root = Tk()
ob = Hospital(root)
root.mainloop()