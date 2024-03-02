#declaring a class 

class Hotelmanage:

#constructor class

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):
        print ("\n========WELCOME TO HOTEL INNOVATION=======\n")
        print("")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

#taking input from the user

    def inputdata(self):
        self.name=input("\nEnter your Fullname:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")

#displaying choices for different rooms available according to price range and calculating room rent
#using if-elif-else for entering user's choice

    def roomrent(self):
        print ("We have the following rooms for you:-")
        print ("1.  Class A---->4000")
        print ("2.  Class B---->3000")
        print ("3.  Class C---->2000")
        print ("4.  Class D---->1000")
        x=int(input("Enter the number of your choice Please->"))
        n=int(input("For How Many Nights Did You Stay:"))
        if(x==1):
            print ("You have choose room Class A")
            self.s=4000*n
        elif (x==2):
            print ("You have choose room Class B")
            self.s=3000*n
        elif (x==3):
            print ("You have choose room Class C")
            self.s=2000*n
        elif (x==4):
            print ("You have choose room Class D")
            self.s=1000*n
        else:
            print ("Please choose a room")
        print ("your choosen room rent is =",self.s,"\n")

#displaying food menu and calculating total cost of food

    def foodpurchased(self):
        print("=======FOOD MENU=======")
        print("1.Dessert----->100","2.Drinks----->50","3.Breakfast--->90","4.Lunch---->110","5.Dinner--->150","6.Exit")
        while (1):
            ch=int(input("Enter the number of your choice:"))
            if (ch==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d
            elif (ch==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d
            elif (ch==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d
            elif (ch==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d
            elif (ch==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d
            elif (ch==6):
                break;
            else:
                print("Pleasr enter a valid option")
        print ("Total food Cost=Rs",self.r,"\n")

#displaying the total cost of the customer with their details

    def display(self):
        print ("=======HOTEL BILL=======")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total Purchased is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grand total Purchased is:",self.rt+self.a,"\n")
        self.rno+=1

#displaying choices to continue entering details or exit
#using if-elif to take choice input from the user

def main():
    a=Hotelmanage()
    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Food Purchased")
        print("4.Show total cost")
        print("5.Exit")
        b=int(input("\nEnter the number of your choice:"))
        if (b==1):
            a.inputdata()
        elif (b==2):
            a.roomrent()
        elif (b==3):
            a.foodpurchased()
        elif (b==4):
            a.display()
        elif (b==5):
            exit()
main()
