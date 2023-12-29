#importing date and time to display on bill
from datetime import datetime

name=input("enter your name:")

#list of items
lists='''
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 20/kg
Oil      Rs 80/kg
Paneer   Rs 110/kg
Maggi    Rs 50/packet
Boost    Rs 90/piece
Colgate  Rs 85/piece
'''

#Declarition
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]

#placing items in dictionary
items={
    'Rice':20,
'Sugar':30,
'Salt':20,
'Oil':80,
'Paneer':110,
'Maggi':50,
'Boost':90,
'Colgate':85
}
option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter Quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
        if finalprice!=0:
            print(25*"=","Anand SuperMarket",25*"=")
            print(28*" ","kannayagudem")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("SNO",10*" ","ITEMS",10*" ","QUANTITY",10*" ","PRICE")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],10*" ",qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ",'Total Amount:','Rs',totalprice)
            print("GST Amount",53*" ",'Rs',gst)
            print(75*"-")
            print(51*" ",'Final Price:','Rs',finalprice)
            print(75*"-")
            print(25*" ","Thanks Visit Again",25*" ")
            print(75*"-")


