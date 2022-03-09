# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3VY2u7g1WBBRZ0bQwzSjpI8hT6nd-9R
"""

print("                  WELCOME TO                           ")
print("               HARRY AND SHERRY")
print("               ICE CREAM PARLOUR                      ")


from tabulate import tabulate
import datetime 
menu={"vanilla ice cream":120, "strawberry ice cream":120, "caramel ice cream":120, "waffle cone":190 , "waffle bowl": 190  ,"vanilla shake":270, "choco shake":270,
      "strawberry shake":270  ,"butterscotch shake":270  ,"cold coffee": 270  , "brownie ice cream":220 ,"cookie small":70 , "cookie large":100 ,"chipwich":190 ,
      "mini sundae":180 ,"sundae":280 ,"tea":120 ,"coffee":200 ,"water":30} #Our menu stored in dictionary.
menu2=[["Vanilla ice cream","Strawberry cream","Caramel ice cream","Waffle cone","Waffle bowl","Vanilla shake","Choco shake","Strawberry shake","Butterscotch shake",
        "Cold coffee","Brownie ice cream","Cookie small","Cookie large","Chipwich","Mini sundae","Sundae","Tea","Coffee","Water"],
       ["120","120","120","190","190","270","270","270","270","270","220","70","100","190","180","280","120","200","30"]]
duty={"1":"Ammar Gullu","2":"Shajeeh Butt"} #shift of the person on duty
temp_discount=0
service=0
grand_total=0
sub_total=0
gst=0.17   #gst=17% nowadays on all food related products
discount_rate=0.10
discount=0
reset="yes"  #initially set the reset to yes so that it executes once
var=0
ext=9
time=input("Enter 1 for 1st shift or 2 for 2nd shift: ")
while time not in duty: #used while loop:if incorrect shift is entered it asks user to enter the shift again.
  print("Wrong instruction")
  time=input("Enter 1 for 1st shift or 2 for 2nd shift again: ")

while reset=="yes": #as initiallized earlier, reset is yes for the first iteration later it can be changed
  sub_total=0
  gst_amount=0
  count=0
  mod=input("Enter bill to generate bill or enter setting to open system settings: ")
  mod=mod.lower()
  while True: #applied an infinite loop
    if mod=="bill": #if input is bill followings set of conditions will run.
      if var==0: # 
        print("Enter close to exit: ")  #this statment will only be shown once while the program is executed under bill
        var=var+1
      if count==0: #first product entry is like below
        prod_name=input("Enter product name : ")
        prod_name=prod_name.lower()
        if prod_name=="close": #whenever close is entered in prod_name the program will end
          break
      else:     #except the first iteration of this while loop this will be used as a statement to enter product names 
       prod_name=input("Enter product name or enter done to conclude : ")
       prod_name=prod_name.lower()
       if prod_name=="close": 
          break
      if prod_name=="done" and count>=1: #user can only enter done when the count is greater then one and boom the program will move to the finishing steps
        if prod_name=="close": 
          break
        dinein=input("If dine-in enter yes else no: ")  #asking dine-in if yes then it will add service charges which are 10%.
        dinein=dinein.lower()
        if dinein=="yes": 
         service=0.10*sub_total
         grand_total=grand_total+service
        pay=input("Payment through card or cash (note: 10% discount on card payment): ")
        pay=pay.lower()  #keeping all in lower case
        if pay=="card": 
         discount=sub_total*discount_rate  #here we add the service charges
         grand_total=grand_total-discount
        break
      elif prod_name not in menu:   # now if the product is not in the decleared dicionary we can add it if needed. 
       print("Product not found in the system")
       add=input("Use extension 4 in system settings to add the product or enter yes to add it now ")
       add=add.lower()
       if add=="yes":
         price=eval(input("Enter the price of the product price: "))
         menu.update({prod_name:price})
         price=menu[prod_name]   
         temp=eval(input("Enter quantity: "))  
         sub_total=price*temp+sub_total
         gst_amount=sub_total*gst   
         grand_total=sub_total+gst_amount
        
         break
      else:
         if prod_name=="close":
          break
         price=menu[prod_name]  #here it will store the price of the product
         temp=eval(input("Enter quantity: "))  # simply asking for quantity
         sub_total=price*temp+sub_total
         table=[["Product","Price/Unit","Quantity","Total"],[prod_name,price,temp,price*temp]]
         print(tabulate(table))
         gst_amount=sub_total*gst  #calculating gst
         grand_total=sub_total+gst_amount
         count=count+1
    elif mod=="setting":  #now we come to the system settings part of our program (if setting is entered instead of bill)
     print("Welcome to system settings")                                                        #here program will ask for the desired extension
     ext=eval(input("Enter desired extension or press 1 to know the extensions or 0 to exit:")) #if extensions are unknow 1 will display all possible extensions.
     if ext==0:
       break
     elif ext==1:
      print("System Setting extensions are")
      print(" ext 0 to exit ")
      print(" ext 1 for extensions detail ")
      print(" ext 2 for updating the price of any product")
      print(" ext 3 for deleting any product")
      print(" ext 4 for adding a product")
      print(" ext 5 for printing out all products  and their prices")
      print(" ext 6 for updating  General sales tax(GST)  ")
     elif ext==2:
      prod_name=input("Enter the name of the product to update its price : ")
      prod_name=prod_name.lower()
      newprice=eval(input("Enter the new price of the product "))
      menu.update({prod_name:newprice})
     elif ext==3:
      prod_name=input("Enter the name of the product to delete it from the system: ")
      prod_name=prod_name.lower()
      menu.pop(prod_name)
      print(prod_name,"Deleted from the system")
     elif ext==4:
       prod_name=input("Enter the name of the product to add it into the system: ")
       prod_name.lower()
       price=eval(input("Enter the price of the product price: "))
       price=price.lower()
       menu.update({prod_name:price}) 
     elif ext==5:
       print(tabulate(menu2))
     elif ext==6:
       tempgst=eval(input("Enter new GST rate without %:"))
       gst=tempgst/100
       break
     else:
       print("Wrong Extension")
       break
    else:
     print("Wrong selection")  # if input is neither bill nor setting then this is the output
     break
  if count>=1:
   if prod_name=="close":
    break
   print("Sub-total = ",sub_total)
   print("General sales tax(GST) =",gst_amount)
   print("Service Charges =",service)
   print("Discount    =",discount)
   print("Grand total =",grand_total,"Rupees")
   today = datetime.datetime.now()
   cash_recieved=eval(input("Enter the cash recieved: "))
   while cash_recieved<grand_total:
     print("Recieved cash cannot be less than Grand Total")
     cash_recieved=eval(input("Enter recieved cash again: "))
   change=cash_recieved-grand_total
   print("Cash Recieved:  ",cash_recieved )
   print("Grand Total:    ",grand_total)
   print("Change:         ",int(change))
   print("Date:", today)
  onduty=duty[time]
  print("Cashier name: ",onduty)
  reset=input("Enter yes to reset or no to exit: ")
  reset=reset.lower()
if reset=="no":   #when reset is no then the program will be finished
   print("Thank you ")