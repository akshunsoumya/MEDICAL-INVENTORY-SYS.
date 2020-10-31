from tkinter import *
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil #The shutil module helps you automate copying files and directories.
import datetime #The datetime module is used to modify date and time objects in various ways.
#defination of subbuttons(def of MEDICINE BLOCK)
def add_medicine():
	with open('medicine.csv','a+') as csvfile:
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'comp_name', 'sup_id','to_pur']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		
		medi_name = input("Enter medicine name : ")
		with open('medicine.csv','r+') as csfile:
			reader=csv.DictReader(csfile)
			

		med_id = input("Enter ID : ")
		sale = float(input("Enter sale price : "))
		unit = float(input("Enter cost price : "))
		quantity = int(input("Enter quantity : "))
		min_quantity = int(input("Enter min quantity to maintain : "))
		comp_name = input("Enter company name : ")
		sup_id = input("Enter supplier ID : ")
		cost = unit * quantity
		to_pur = min_quantity - quantity
		if quantity >min_quantity:
			to_pur = 0
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'unit':unit,'quantity':quantity,\
		'min_quantity':min_quantity,'comp_name':comp_name,'sup_id':sup_id,'to_pur':to_pur})

		
		with open('purchase.csv','a+') as csvfile:
			pur_date= d.strftime("%d")
			pur_month= d.strftime("%m")
			pur_year = d.strftime("%Y")
			columns = ['medi_name','med_id','unit','quantity','pur_date', 'pur_month','pur_year','sup_id','cost']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			
			writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':pur_date,'pur_month':pur_month,'pur_year':pur_year,'sup_id':sup_id,'cost':cost})
#defination of subbbuton under the medicine block(i.e= SEARCH MEDICINE)
def search_medicine():
    with open('medicine.csv','r') as csvfile:
        name=input('Enter the medicine to search : ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'] == name:
                print(' Name :', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Price : ',row['sale'])	
#defination of subbuton under the Medicine block (UPDATE MEDICINE)
def update_medicine():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['medi_name','med_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_pur']
    with open('medicine.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        med_name =input('Enter the name of the medicine you want to modify : ')
        for row in reader:
            if row['medi_name'] == med_name:
            	print('---------------------------------------------')
            	print('|1.To update Name                           |')
            	print('---------------------------------------------')
            	print('|2.To update Cost price                     |')
            	print('---------------------------------------------')
            	print('|3.To update Sale price                     |')
            	print('---------------------------------------------')
            	print('|4.To update supplier ID                    |')
            	print('---------------------------------------------')
            	choice=int(input())
            	if(choice==1):
            		row['medi_name']=input("Enter the new name : ")

            	elif(choice==2):
            		row['cost']=input("Enter the new cost price : ")

            	elif(choice==3):
            		row['sale']=input("Enter the new sale price : ")

            	elif(choice==4):
            		row['sup_id']=input("Enter the new supplier ID : ")    
            row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
		    'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_pur':row['to_pur']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'medicine.csv')



#Defination of the sub button under the Medicine Block(MEDICINE TO BE PURCHASED)
def medicine_to_be_purchased():
   
	with open('medicine.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
				print(' Name : ', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Minimum Quantity : ',row['min_quantity']\
				,'\n','To be purchased : ',row['to_pur'],'\n','Supplier ID : ',row['sup_id'])   
		
 #defination of B1(MEDICINE) main
# medicine Menu   
    
def B1fun():
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('350x200')
    medicine_menu_window.title("Pharmacy Management Software")
    def destroy():
         medicine_menu_window.destroy()
    lbl = Label(medicine_menu_window, text="Medicine Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(medicine_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(medicine_menu_window, text="Add New Medicine", fg="red",command=add_medicine)
    btn1.grid(column=0, row=2)
    btn2 = Button(medicine_menu_window, text="Search Medicine", fg="red",command=search_medicine )
    btn2.grid(column=0, row=3)
    btn3 = Button(medicine_menu_window, text="Update Medicine", fg="red",command=update_medicine)
    btn3.grid(column=0, row=4)
    btn4 = Button(medicine_menu_window, text="Medicines to be purchased", fg="red",command=medicine_to_be_purchased)
    btn4.grid(column=0, row=5)
    btn5 = Button(medicine_menu_window, text="Return to main menu", fg="red",command=destroy)
    btn5.grid(column=0, row=6)
    medicine_menu_window.mainloop()
#################################################################################################################################
#defination from the B2 button and(NEW CUSTOMER)# FOR TE NEW CUSTOMER

    
    
# defination of B2(CUSTOMER PORTAL) main
# Customer Menu
def B2fun():
    c_menu_window = Tk()
    c_menu_window.geometry('350x200')
    c_menu_window.title("Pharmacy Management Software")
    def destroy():
        c_menu_window.destroy()
    lbl = Label(c_menu_window, text="Customer Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(c_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(c_menu_window, text="Search Customer", fg="red",command=search_customer)
    btn1.grid(column=0, row=2)
    btn2 = Button(c_menu_window, text="New Customer", fg="red",command=new_customer)
    btn2.grid(column=0, row=3)
    btn3 = Button(c_menu_window, text="Update Customer Info", fg="red",command=update_customer)
    btn3.grid(column=0, row=4)
    btn4 = Button(c_menu_window, text="Return to main menu", fg="red",command=destroy )
    btn4.grid(column=0, row=5)
    c_menu_window.mainloop()
################################################################################################################################
#defination of B3(SUPPLIER MENU)
def B3fun():
    s_menu_window = Tk()
    s_menu_window.geometry('350x200')
    s_menu_window.title("Pharmacy Management Software")
    def destroy():
        c_menu_window.destroy()
    lbl = Label(s_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(s_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(s_menu_window, text="Search Supplier",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(s_menu_window, text="New Supplier",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(s_menu_window, text="Update Supplier Info",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn4 = Button(s_menu_window, text="Return to main menu",fg="red", command=destroy)
    btn4.grid(column=0, row=5)
    s_menu_window.mainloop()

#################################################################################################################################    
#defnination of B4(PATIENT DATABASE)
def B4fun():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.title("Pharmacy Management Software")
    def destroy():
        c_menu_window.destroy()
    lbl = Label(r_menu_window, text="Patient Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(r_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(r_menu_window, text="New Patient",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(r_menu_window, text="Discharge patient",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(r_menu_window, text="Number of beds Available",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn3 = Button(r_menu_window, text="Total ammout to be paid",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=5)
    btn3 = Button(r_menu_window, text="Profit Report",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=6)
    btn4 = Button(r_menu_window, text="Return to main menu",fg="red", command=destroy)
    btn4.grid(column=0, row=7)
    r_menu_window.mainloop()
################################################################################################################################
#defnination of B4(INSTRUCTIONS/SUGGESTIONS)
def B5fun():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.config(bg="#232528")
    r_menu_window.title("Pharmacy Management Software")
    def destroy():
        r_menu_window.destroy()
    lbl = Label(r_menu_window, text="Instructions!")
    lbl.grid(row=1,column=2)
    txt1 = Text(a,font=("consolas",12),bg="#232528",fg="white",height=3,width=33)
    txt1.insert(END, "Here you have to select one \nalgorithm to solve the maze and  check the random maze if you wish not to make on yourself and press PROCEED.")
    txt1.place(x=0,y=60)
    btn4 = Button(r_menu_window, text="Return to main menu",fg="red", command=destroy)
    btn4.place(x=10,y=150)
    r_menu_window.mainloop()

#################################################################################################################################
# Main menu
def main_menu():
    
    top = Tk()
    top.geometry("400x400")
    top.title("_MEDICAL INVENTORY MANAGMENT_")
    top.config(bg="#232528")
    L = Label(text="Where do you want to visit")
    L.grid(row=2, column=2)
    B1 = Button(text="MEDICINE", activebackground="red", bg="white", activeforeground="black", command=B1fun)
    B1.grid(row=3, column=4)
    B2 = Button(text="CUSTOMER PORTAL", activebackground="red", bg="white", activeforeground="black", command=B2fun)
    B2.grid(row=6, column=4)
    B3 = Button(text="SUPPLIER MENU", activebackground="red", bg="white", activeforeground="black",command=B3fun)
    B3.grid(row=8, column=4)
    B4 = Button(text="PATIENT DATABASE", activebackground="red", bg="white", activeforeground="black",command=B4fun)
    B4.grid(row=10, column=4)
    B5 = Button(text="INSTRUCTIONS/SUGGESTIONS", activebackground="red", bg="white", activeforeground="black",command=B5fun)
    B5.grid(row=12, column=4)
    top.mainloop() 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def window():
    top=Tk()
    top.geometry("100x100")
    top.title("_MEDICAL INVENTORY MANAGMENT_")
    top.config(bg="#232528")
    L=Label(text="WELCOME TO THE INVENTORY MANAGMENT SOFTWARE ^^^^")
    L.grid(row=2, column=2)
    B2 = Button(text="CLICK TO START", activebackground="red", bg="white", activeforeground="black", command=B2fun)
    B2.grid(row=6, column=4)
    
main_menu()