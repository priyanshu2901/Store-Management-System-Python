#import necessary header files
from tkinter import *
import time
import mysql.connector
from tkinter import messagebox
import datetime
master = Tk()#create GUI object
#Global variable ussed to store data
var_id=StringVar()
var_qty=StringVar()
p_name=StringVar()
ph_no=StringVar()
flag=4
total=0

def createDatabase():#function to create the database
        
    mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345')#string to connect to database
    mycursor=mydb.cursor()
    mycursor.execute('create database if not exists store')#execute the sql querry(create database)
    mydb.close()#close the database
    
    try:
        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')#open the database
        mycursor=mydb.cursor()
        #create all the necessary table if they are not exist
        mycursor.execute("create table if not exists shipping(Product_Number int not null,Number_of_Units int not null,Whole_Sale_Price decimal(8,2) not null,Exp_date varchar(255) default 'n/a')")
        mycursor.execute("create table if not exists Product(Product_Number int not null ,Product_Name varchar(255) not null,Product_Description varchar(255) not null,Product_Unit_Price decimal(8,2) not null)")
        mycursor.execute("create table if not exists sales(Sale_Product_Name varchar(255) not null,Number_of_Units int not null,TotalPrice decimal(8,2) not null,SellingDate date not null)")
        mycursor.execute("create table if not exists orderList(Product_Number int not null)")

        
    except Exception as e:
        print('something went wrong',e)
        messagebox.showinfo('Messsage',"dtabase cannot be creataed")#show error when an exception is occured

        
    finally:
        mydb.close()#close the database
def salesReport():
    global master#import master object
    #to cleare the master window
    list = master.grid_slaves()
    for l in list:
        l.destroy()
    
    try:
        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')#create conection to database
        mycursor=mydb.cursor()
        mycursor.execute("select * from sales")#execute sql querry
        
        obj=mycursor.fetchall()# fetch all the data
        row_count=len(obj)#find how many rows are there inn fetched data
        if(row_count==0):#if number of rows is 0
            messagebox.showinfo('Messsage','No Record Found')# show error message
            GUI()#call the GUI function
        else:
            total=0;#initialize total=0 
            label1=Label(master,text='Product Name',width=15,font= "Verdana 11 bold")#create lable
            label1.grid(row=0,column=0,sticky=W,padx=10, pady=10)#set the lable in master window
            label1=Label(master,text='Number of units',width=25,font= "Verdana 11 bold")#create the lable
            label1.grid(row=0,column=1,sticky=W,padx=10, pady=10)#set the lable in master window
            label1=Label(master,text='Total Price',width=15,font= "Verdana 11 bold")#create lable
            label1.grid(row=0,column=2,sticky=W,padx=10, pady=10)#set the lable in master window
            label1=Label(master,text='Selling Date',width=15,font= "Verdana 11 bold")#crete lable
            label1.grid(row=0,column=3,sticky=W,padx=10, pady=10)#set lable in master window
            
            i=0#initialize i=0
    
            
            while(i<row_count):
                
                label2=Label(master,text=obj[i][0],width=15,font= "Verdana 10")#create lable
                label2.grid(row=i+1,column=0,padx=5, pady=5)#set lable in master window
                label3=Label(master,text=obj[i][1],width=25,font= "Verdana 10")#create lable
                label3.grid(row=i+1,column=1,padx=5, pady=5)#set lable in master window
                label4=Label(master,text=obj[i][2],width=15,font= "Verdana 10")#create lable
                label4.grid(row=i+1,column=2,padx=5, pady=5)#set lable in master window
                label5=Label(master,text=obj[i][3],width=15,font= "Verdana 10")#create lable
                label5.grid(row=i+1,column=3,padx=5, pady=5)#set lable in master window
                total+=obj[i][1]#increase total 
                i=i+1
                
            label1=Label(master,text='Total Unit : ',width=15,font= "Verdana 11 bold")#create lable
            label1.grid(row=i+1,column=2,padx=2, pady=2)#set lable in master window
            
            label5=Label(master,text=total,width=15,font= "Verdana 10")#create lable
            label5.grid(row=i+1,column=3,padx=2, pady=2)#set lable in master window
                
            b1=Button(master,text='BACK ',font= "Verdana 10 ",command=GUI, height=1, width=5,relief="groove",bd=3)#create button
            b1.grid(row=i+2,column=3,padx=2, pady=2)#set button in master window
            master.mainloop()
    except Exception as e:
        print('something went wrong',e)
    finally:
        mydb.close()#close connection

def stockReport():#function to show report
    global master#call global
    #to cleare the master window
    list = master.grid_slaves()
    for l in list:
        l.destroy()
    
    try:
        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')#create connection
        mycursor=mydb.cursor()
        mycursor.execute("select * from shipping")#execute querry
        
        obj=mycursor.fetchall()#fetch data
        row_count=len(obj)#count number of rows in fetched data
        if(row_count==0):
            messagebox.showinfo('Messsage','No Record Found')
            GUI()
        else:
            
            label1=Label(master,text='Product Number',width=15,font= "Verdana 11 bold")#create label
            label1.grid(row=0,column=0,sticky=W,padx=10, pady=10)#set label in master window
            label1=Label(master,text='Number of units',width=25,font= "Verdana 11 bold")#create label
            label1.grid(row=0,column=1,sticky=W,padx=10, pady=10)#set label in master window
            label1=Label(master,text='Whole Sale Price',width=15,font= "Verdana 11 bold")#create label
            label1.grid(row=0,column=2,sticky=W,padx=10, pady=10)#set label in master window
            label1=Label(master,text='Exp Date',width=15,font= "Verdana 11 bold")#create label
            label1.grid(row=0,column=3,sticky=W,padx=10, pady=10)
            
            i=0
    
            
            while(i<row_count):
                
                label2=Label(master,text=obj[i][0],width=15,font= "Verdana 10")#create label
                label2.grid(row=i+1,column=0,padx=5, pady=5)#set label in master window
                temp=obj[i][0]
                label3=Label(master,text=obj[i][1],width=25,font= "Verdana 10")#create label
                
                label3.grid(row=i+1,column=1,padx=5, pady=5)#set label in master window
                label4=Label(master,text=obj[i][2],width=15,font= "Verdana 10")#create label
                label4.grid(row=i+1,column=2,padx=5, pady=5)#set label in master window
                label5=Label(master,text=obj[i][3],width=15,font= "Verdana 10")#create label
                label5.grid(row=i+1,column=3,padx=5, pady=5)#set label in master window
                
                if(obj[i][1]<10):#check if number of units is less than 10
                    #add the product number in orderList Table
                    mycursor.execute("select * from orderList where Product_Number='%s'"%(temp))
                    obj2=mycursor.fetchall()    
                    row_count2=len(obj2)
                    if(row_count2==0):
                        mycursor.execute("insert into orderList(Product_Number)values('%s')"%(temp))
                        mydb.commit()
                        
            
                i=i+1
            b1=Button(master,text='BACK ',font= "Verdana 10 ",command=GUI, height=1, width=5,relief="groove",bd=3)#create button
            b1.grid(row=i+2,column=3,padx=2, pady=2)#set button
            master.mainloop()
    except Exception as e:
        print('something went wrong',e)
    finally:
        mydb.close()

def shipProduct(): #function to add shipping product
    def sub_insert():#local function for sub menu
     if(get_number.get().isdigit()):#check if product number is digit or not
         if(get_unit.get().isdigit()):# check unit is digit or not
             if(len(get_price.get())>0):#check price has value or not
                if(len(get_Exp.get())>7) and get_Exp.get()[2]=='-' and get_Exp.get()[5]=='-': #check date is in correct format or not
                   try:
                        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')#open connection
                        mycursor=mydb.cursor()
                        #add record to shipping table
                        mycursor.execute("insert into shipping(Product_Number,Number_of_Units,Whole_Sale_Price,Exp_date)values('%s','%s','%s','%s')"%(get_number.get(),get_unit.get(),get_price.get(),get_Exp.get()))
                        mydb.commit()
                        result=messagebox.showinfo('Messsage','record added')
                        if(result=='ok'):
                            GUI()#call GUI function
                   except Exception as e:
                           messagebox.showinfo('Messsage',e)
                   finally:
                            mydb.close()#close connection
                else: 
                      try:
                          #open connection
                        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')
                        mycursor=mydb.cursor()
                        #add record to shipping table
                        mycursor.execute("insert into shipping(Product_Number,Number_of_Units,Whole_Sale_Price)values('%s','%s','%s')"%(get_number.get(),get_unit.get(),get_price.get()))
                        mydb.commit()
                        result=messagebox.showinfo('Messsage','record added with default expiry date')
                        if(result=='ok'):
                            GUI()#call GUI function
                      except Exception as e:
                           messagebox.showinfo('Messsage',e)
                      finally:
                            mydb.close()#close connection
             else:
               messagebox.showinfo('Messsage','Enter correct Price')
         else:
             messagebox.showinfo('Messsage','Enter Correct unit price ')
     else:
         messagebox.showinfo('Messsage','Enter correct number')
        
    global master#call global object
    #to cleare the master window
    list = master.grid_slaves()
    for l in list:
        l.destroy()
        
    label_number=Label(master,text="Product Number",font= "Verdana 10")#create label
    label_unit=Label(master,text="Number of units",font= "Verdana 10")#create label
    label_price=Label(master,text="Whole sale price ",font= "Verdana 10")#create label    
    label_Exp=Label(master,text="Expiry Date (dd-mm-yyyy)",font= "Verdana 10")#create label    
    
    get_number=Entry(master,relief="groove")#to take single line user input
    get_unit=Entry(master,relief="groove")#to take single line user input
    get_price=Entry(master,relief="groove")#to take single line user input
    get_Exp=Entry(master,relief="groove")#to take single line user input
    
    label_number.grid(row=0,sticky=E,padx=10, pady=10)#set label
    label_unit.grid(row=1,sticky=E,padx=10, pady=10)#set label
    label_price.grid(row=2,sticky=E,padx=10, pady=10)#set label
    label_Exp.grid(row=3,sticky=E,padx=10, pady=10)#set label
    
    get_number.grid(row=0,column=1,sticky=W,padx=10, pady=10)#set Entry 
    get_unit.grid(row=1,column=1,sticky=W,padx=10, pady=10)#set Entry 
    get_price.grid(row=2,column=1,padx=10, pady=10)#set Entry 
    get_Exp.grid(row=3,column=1,sticky=W,padx=10, pady=10)#set Entry 
    
    
    
    
    b1=Button(master,text='ADD\nRECORD',command=sub_insert ,font= "Verdana 10 ",relief="groove",bd=3,activebackground='black')#create button
    b1.grid(column=1,padx=10, pady=10,sticky=E)#set button 
    b2=Button(master,text='BACK',command=GUI,font= "Verdana 10 ", height=1, width=5,relief="groove",bd=3,activebackground='black')#create button
    b2.grid(column=1,padx=10, pady=10,sticky=E)#set button 
    master.mainloop()

def registerProduct():#function to register product
    global master
    #to cleare the master window
    list = master.grid_slaves()
    for l in list:
        l.destroy()
    
    def sub_insert():#local function
     if(get_number.get().isdigit()):#check product number is digit or not
         if(len(get_name.get())>0):#check product name has value or not
             if(len(get_desc.get())>0):#check description has value or not
                if(len(get_unit.get())>0): #check unit has value or not
                   try:
                       #open connection
                        mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from Product where Product_Number='%s'"%get_number.get())
                        obj=mycursor.fetchall()    
                        row_count=len(obj)
                        if(row_count>0):#check record already added or not
                             messagebox.showinfo('Messsage','Record Already added')
                        else:
                            #insert record in  product table
                            mycursor.execute("select * from shipping where Product_Number='%s'"%get_number.get())
                            obj=mycursor.fetchall()    
                            row_count=len(obj)
                            if(row_count>0):
                                mycursor.execute("insert into product(Product_Number,Product_Name,Product_Description,Product_Unit_Price)values('%s','%s','%s','%s')"%(get_number.get(),get_name.get(),get_desc.get(),get_unit.get()))
                                mydb.commit()
                                result=messagebox.showinfo('Messsage','record added')
                                if(result=='ok'):
                                    GUI()#call GUI function
                            else:
                                messagebox.showinfo('Messsage','Product number not found')
                   except Exception as e:
                           messagebox.showinfo('Messsage',e)
                   finally:
                            mydb.close()#close connection
                else: 
                     messagebox.showinfo('Messsage','Enter correct Unit Price')
             else:
               messagebox.showinfo('Messsage','Description cannot be empty')
         else:
             messagebox.showinfo('Messsage','Name cannot be empty')
     else:
         messagebox.showinfo('Messsage','Enter correct number')
         
    label_number=Label(master,text="Product Number",font= "Verdana 10")#create label
    label_name=Label(master,text="Product Name",font= "Verdana 10")#create label
    label_desc=Label(master,text="Product Description ",font= "Verdana 10")    #create label
    label_unitprice=Label(master,text="Unit Price",font= "Verdana 10")    #create label
    
    get_number=Entry(master,relief="groove")#to take single line user input
    get_name=Entry(master,relief="groove")
    get_desc=Entry(master,relief="groove")
    get_unit=Entry(master,relief="groove")
    
    label_number.grid(row=0,sticky=E,padx=10, pady=10)#set label
    label_name.grid(row=1,sticky=E,padx=10, pady=10)#set label
    label_desc.grid(row=2,sticky=E,padx=10, pady=10)#set label
    label_unitprice.grid(row=3,sticky=E,padx=10, pady=10)#set label
    
    get_number.grid(row=0,column=1,sticky=W,padx=10, pady=10)#set entry
    get_name.grid(row=1,column=1,sticky=W,padx=10, pady=10)
    get_desc.grid(row=2,column=1,padx=10, pady=10)
    get_unit.grid(row=3,column=1,sticky=W,padx=10, pady=10)
    
    
    
    
    b1=Button(master,text='ADD\nRECORD',command=sub_insert ,font= "Verdana 10 ",relief="groove",bd=3,activebackground='black')
    b1.grid(column=1,padx=10, pady=10,sticky=E)#set button
    b2=Button(master,text='BACK',command=GUI ,font= "Verdana 10 ", height=1, width=5,relief="groove",bd=3,activebackground='black')
    b2.grid(column=1,padx=10, pady=10,sticky=E)#set button
    master.mainloop()
        
    


def bill():#function for billing
 #call global variable
 global total
 global cost
 total=0
 
 global master
 #to cleare the master window
 list = master.grid_slaves()
 for l in list:
        l.destroy()
    
 def print_rec():#local function to print record
     try:
         if(total==0):
             result=messagebox.showinfo('message','NOTHING TO PRINT')
             if(result=='ok'):
                 GUI()#call GUI function
         result=messagebox.showinfo('message','record printed')
         if(result=='ok'):
             GUI()#call GUI function
     except Exception as e:
         print(e)
     finally:
         pass
                    
 def zipzap():#function to add item to the billing list
     
     global total
     global cost
     try:
         global flag
         #open connection
         mydb=mysql.connector.connect(host='localhost',username='root',passwd='12345',database='store')
         mycursor=mydb.cursor()
         
         
         if(var_id.get().isdigit()):#check product number is digit or not
             if(len(var_qty.get())>0 ):#check qantity has value or not

                 mycursor.execute("select * from product where Product_Number='%s'"%var_id.get())#done to check Product id is valid or not 
                 obj=mycursor.fetchall()    
                 row_count=len(obj)
                 if(row_count>0):
                     #fetch data from product and shipping table
                     mycursor.execute("select s.product_number,product_name,product_Description,Product_Unit_Price from shipping s, Product p where p.Product_Number=s.Product_Number and Number_of_Units>='%s' and s.product_Number='%s'"%(int(var_qty.get()),var_id.get()))
                     obj=mycursor.fetchall()
                     if(len(obj)==1):
                         i=0
                         while(i<row_count):
                             
                             label2=Label(master,text=obj[i][0],width=15,font= "Verdana 10")#create label
                             label2.grid(row=flag,column=0,padx=5, pady=5,columnspan=2)#set label
                             label3=Label(master,text=obj[i][1],width=25,font= "Verdana 10")#create label
                             label3.grid(row=flag,column=2,padx=5, pady=5,columnspan=3)#set label
                             label4=Label(master,text=obj[i][2],width=15,font= "Verdana 10")#create label
                             label4.grid(row=flag,column=6,padx=5, pady=5)#set label
                             label5=Label(master,text=obj[i][3],width=15,font= "Verdana 10")#create label
                             label5.grid(row=flag,column=7,padx=5, pady=5)#set label
                             price=float( obj[i][3])*float(var_qty.get())#to get price
                             
                             total=total+price
                             
                             label6=Label(master,text=var_qty.get(),width=15,font= "Verdana 10")#create label
                             label6.grid(row=flag,column=8,padx=5, pady=5)#set label
                             
                             label7=Label(master,text=price,width=15,font= "Verdana 10")#create label
                             label7.grid(row=flag,column=9,padx=5, pady=5)#set label
                             
                             label7=Label(master,text='TOTAL',width=15,font= "Verdana 10")#create label
                             label7.grid(row=flag+1,column=8,padx=5, pady=5)#set label
                             
                             label7=Label(master,text=total,width=15,font= "Verdana 10")#create label
                             label7.grid(row=flag+1,column=9,padx=5, pady=5)#set label
                             
                             
                             label7=Label(master,text='TAX(13%)',width=15,font= "Verdana 10")#create label
                             label7.grid(row=flag+2,column=8,padx=5, pady=5)#set label
                             
                             tax=total
                             tax=(total*13)/100#to calculate tax
                             
                             label7=Label(master,text=tax,width=15,font= "Verdana 10")
                             label7.grid(row=flag+2,column=9,padx=5, pady=5)#set label
                             
                             label7=Label(master,text='Total',width=15,font= "Verdana 10")
                             label7.grid(row=flag+3,column=8,padx=5, pady=5)
                             label7=Label(master,text=total+tax,width=15,font= "Verdana 10")
                             label7.grid(row=flag+3,column=9,padx=5, pady=5)
                             
                             
         
                             flag=flag+1
                             i=i+1
                         #update the changes to the tabel
                         mycursor.execute("UPDATE shipping SET Number_of_Units = Number_of_Units-'%s' WHERE product_number='%s' "%(var_qty.get(),int(var_id.get())))
                         mydb.commit()
                     
                         mycursor.execute("insert into sales(sale_product_name,Number_of_Units,TotalPrice,SellingDate) values('%s','%s','%s','%s')"%(obj[i-1][1],var_qty.get(),price,datetime.datetime.now()))
                         mydb.commit()
                         messagebox.showinfo('message','RECORD ADDED')
                         
                     
                         
                         
                     else:
                         messagebox.showinfo('message','product out of stock')
                    
                 else:
                     messagebox.showinfo('message','product not found')
             else:
                 messagebox.showinfo('message','enter valid quantity')
         else:
                messagebox.showinfo('mesage','Wrong or empty ID')

         

     except Exception as e:
         print(e)

     finally:
        mydb.close()
     
 def test():#local function for name and number of customer
    if(len(entry_get_name.get())>0):#check name has value or not
        if(entry_get_phno.get().isdigit() ):#check phno is integer or not
            child = Toplevel(master)
            
            label_get_number = Label(child, text="Product Number : ",font= "Verdana 10 " )#create labe;
            label_get_qty=Label(child,text='Quantity :',font= "Verdana 10 ")#set label
            entry_get_number=Entry(child,textvariable=var_id,relief="groove")
            entry_get_qty=Entry(child,textvariable=var_qty,relief="groove")
            
            label_get_number.grid(row=0,column=0,padx=10, pady=10)#create label
            entry_get_number.grid(row=0,column=1,padx=10, pady=10)#for input
            
            label_get_qty.grid(row=1,column=0,padx=10, pady=10)#set label
            entry_get_qty.grid(row=1,column=1,padx=10, pady=10)#set input
        
            
            b_add=Button(child,text='add',command=zipzap ,font= "Verdana 12 ",relief="groove",bd=3)#create button
            b_back=Button(child,text='back',command=child.destroy ,font= "Verdana 12 ",relief="groove",bd=3)#create button
            
            b_add.grid(row=2,column=0,padx=10,pady=10)#set button
            b_back.grid(row=2,column=1,padx=10,pady=10)    #set button
        else:
            messagebox.showinfo('message','enter correct phno')
    else:
         messagebox.showinfo('message','enter correct name')
    
 label_get_name=Label(master,text='name : ',font= "Verdana 10 ")#create label
 label_get_phno=Label(master,text="Ph No. :",font= "Verdana 10 ")#create label
 entry_get_phno=Entry(master,textvariable=ph_no,relief="groove")#for input
 entry_get_name=Entry(master,textvariable=p_name,relief="groove")#for input

 label_get_name.grid(row=0,column=0,padx=10, pady=10)#set label
 label_get_phno.grid(row=1,column=0,padx=10, pady=10)#set label
 entry_get_name.grid(row=0,column=1,padx=10, pady=10,columnspan=2)#set input
 entry_get_phno.grid(row=1,column=1,padx=10, pady=10,columnspan=2)#set input

 label1=Label(master,text='Product Number',width=15,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=0,sticky=W,padx=10, pady=10,columnspan=2)#set label
 label1=Label(master,text='Product Name',width=25,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=2,sticky=W,padx=10, pady=10,columnspan=3)#set label
 label1=Label(master,text='Product Description',width=15,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=6,sticky=W,padx=10, pady=10)#set label
 label1=Label(master,text='Unit Price',width=15,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=7,padx=10, pady=10)#set label
 label1=Label(master,text='Quantity',width=15,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=8,sticky=W,padx=10, pady=10)#set label
 label1=Label(master,text='TOTAL PRICE',width=15,fg='white',bg='black',font= "Verdana 11 bold")#create label
 label1.grid(row=3,column=9,sticky=W,padx=10, pady=10)#set label



 b1=Button(master,text='add item',command= test ,font= "Verdana 12 ",relief="groove",bd=3)#create button
 b1.grid(row=2,column=0,padx=10,pady=10)#set button
 b2=Button(master,text='BACK',command= GUI ,font= "Verdana 12 ",relief="groove",bd=3,activebackground='black')#create button
 b2.grid(row=2,column=1,padx=10,pady=10)#set button
 b3=Button(master,text='print',command= print_rec ,font= "Verdana 12 ",relief="groove",bd=3)#create button
 b3.grid(row=2,column=2,padx=10,pady=10)#setbuttton



def GUI():#function to create GUI
    global master
    #to cleare the master window
    list = master.grid_slaves()
    for l in list:
        l.destroy()
        
    width=master.winfo_screenwidth()#get screen width
    height=master.winfo_screenheight()#get screen height
    master.geometry('%sx%s'%(width,height))#set width and height of window
    
    b1 = Button(master,text='Register\n Product ',compound=CENTER ,font= "Verdana 15 bold",command=registerProduct,relief="solid",bd=3, width=10,height=5)#create button
    b1.grid(row=1,column=1,padx=10, pady=10)#set button
    
    b1 = Button(master,text='Billing ',compound=CENTER ,font= "Verdana 15 bold",command=bill,relief="solid",bd=3,width=10,height=5)#create button
    b1.grid(row=1,column=2,padx=10, pady=10)#set button
    
    b1 = Button(master,text='Sales\nReport ',compound=CENTER ,font= "Verdana 15 bold",command=salesReport,relief="solid",bd=3,width=10,height=5)#create button
    b1.grid(row=2,column=1,padx=10, pady=10)#set button
    
    b1 = Button(master,text='Shipping\n Product ',compound=CENTER ,font= "Verdana 15 bold",command=shipProduct,relief="solid",bd=3,width=10,height=5)#create button
    b1.grid(row=2,column=2,padx=10, pady=10)#set button
    
    b1 = Button(master,text='Stock\n Report ',compound=CENTER ,font= "Verdana 15 bold",command=stockReport,relief="solid",bd=3,width=10,height=5)#create button
    b1.grid(row=3,column=1,padx=10, pady=10)#set button
    
    b1 = Button(master,text='Exit ',compound=CENTER ,font= "Verdana 15 bold",command=master.destroy,relief="solid",bd=3,width=10,height=5)#create button
    b1.grid(row=3,column=2,padx=10, pady=10)#set button
    
    
    
    master.mainloop()
        
if __name__=="__main__":#main function
    createDatabase()#call create database function
    GUI()#call GUI function
