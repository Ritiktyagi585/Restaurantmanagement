
#i=100
#while(i<1000):
    #if(i==5):
     #   continue
    #i=i+100
   # print(i)
     
#s=input("enter the no.")
#print(s)
#s="DuCaT NoIdA"
#s1=s.upper()
#print(s1)
#s="ducat india"
#s1=s.split()
#print(s1)
#s="india ducat"
#s1=s.replace("india ducat","noida")
#print(s1)
#s="           jai shree ram    "
#s1=s.strip()
#print(s1)
#r="ritik tyagi"
#r1=r.count("i")
#print(r1)
#index()
#find the 1st occurrence of the specified value.
#this method raise an Exception if the value is not found 
#s="ducat india"
#s1=s.index(c) 
#print(s1)
#s="123"
#s1=s.isdigit()
#print(s1)
#s="DuCat InDiA"
#s1=s.swapcase()
#print(s1)
#s="123abc"
#e=s.isalnum()
#print(e)
#s="123"
#s1=s.isalpha()
#print(s1)
#s="python"
#print(s[::-1])
#s="python"
#print(s[1:5:7]) 
#l1=[2,4,1,["hello"],5,5,2,7,8,6]
#l2=[2,6,True]
#l3=l1+l2
#l4=12*3
#print(l1)
#l5=[1,3,5,7,2,9,10]
#l6=[x for x in 15 ]
#print(16)

#Class Account:
#acn=1001
#name="ritik"
#e=Account()
#rint(e
menu = {
    'pizza':40,
    'pasta':50,
    'coffee':60,
    'burger':40,
    'cold drink':80,

}

print("welcome to restaurant")
print("pizza: 40\npasta: 50\ncoffee: 60\nburger: 50\ncold drink :80")

order_total = 0
 
item_1 =input("enter item you want to order =")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item{item_1}has been added to your order")
  

else:
    print(f"order item not available {item_1}yet!")  

another_order = input("Do you want to add another item? (yes/no)") 
if another_order == "yes":
    item_2 = input("enter the name of second item = ") 
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"ordered item {item_2} has been added to order")
else:
    print("ordered item {item_2} is not available")

print(f"the total amount of items to pay is {order_total}")
