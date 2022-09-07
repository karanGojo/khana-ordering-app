import admin as ad# here we have imported the admin file as ad

class user: # we ghav eused class as user
    
    login_info={"karan":"karan@29","karan":"karan@96"}# log info throught which user can log in
    order_history={}#as to add the food items later buy user we have made empty list
    profile = {}#as to add profile of the user.
    
    
    def __init__(self,fullname,phonenumber,email,address,password):# here we have created the instace method as to name the attributes
        self.fullname = fullname
        self.phonenumber=phonenumber
        self.email=email
        self.addresss=address
        self.password=password
    
        
        
        
    @classmethod    #here we ahve use the decorator as to decorate our signup function for the user class.
    def signup(cls,fullname,phonenumber,email,address,username,password):
        user.profile[username]={     # here we have used the empty profile as to store the data of the user(here the profile is a class variable which is been called as by the class that is user,profile[username] )
            "fullname":fullname,
            "phonenumber":phonenumber,
            "email":email,
            "address":address,
            "username":username,
            "password":password,
            }
        user.login_info[username]=password
        print('\n')
        print("  You have successfully registered . Now you can login  ")
        return user.profile
    
    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("   You're are successfully logged in   ")
            return True
        else:
            print("   SORRY! These are the Wrong Credentials   ")
            return False
        
    
    
    
    def place_new_order(self,username):
        Place_order_crawler = True
        while Place_order_crawler:
            l=[]
            print("Select items from below inventory ::")
            print("_______________________________")
            for i in ad.inventory:
                print("{}. {} ({}) [INR {} ]".format(ad.inventory[i]['FoodID'],ad.inventory[i]['Name'],ad.inventory[i]['Quantity'],ad.inventory[i]['Price']))
            a=list(map(int,input("Select the item id which you want to buy separated by comma :: ").split(',')))
            total=0
            for i in a:
                price=0
                b=int(input("Howmany {} you want to buy ".format(ad.inventory[i]['Name'])))
                price+=ad.inventory[i]['Price']*(1-(ad.inventory[i]['Discount']/100))*b
                total+=price
                l.append([ad.inventory[i]['Name'],b,ad.inventory[i]['Price'],ad.inventory[i]['Discount'],price])
            user.order_history[username]=l
            print('\n')
            print("The cart is as follows :: ")
            print("Username :: {}".format(username))
            print('____________________________________')
            for i in user.order_history[username]:
                print("{}--{}Nos--{}INR".format(i[0],i[1],i[4]))
            print('_____________________________________')
            print('Total amount you have to paid {}'.format(total))
            print("Do you want to update your order ?")
            m=int(input("1.Yes 2.No\n enter a key:"))
            if m==2:
                Place_order_crawler=False
        k=int(input("Select Place your order option :: \n 1.Place your order"))
        if k==1:
            print('\n')
           
            print("********************* Your order is placed successfully . ********************* ")
        return True

    def order_history_(self,username):
        total=0
        for i in self.order_history[username]:
            total+=i[4]
            print("Name :: {}".format(i[0]))
            print("________________________________________________________")
            print("Quantity :: {}".format(i[1]))
            print("Price/Quantity:: {}".format(i[2]))
            print("Discount :: {}".format(i[3]))
            print("Toatal price after discount :: {}".format(i[4]))
            print('\n')
        print("Total amount {}".format(total))
        return user.order_history
        
    
        
    def update_profile(self,username):
        fullname=input("Enter your name :: ")
        phonenumber=int(input("Enter your phone number :: "))
        email = input("Enter your email id :: ")
        address=input("Enter your address :: ")
        password=input("Enter your password :: ")
        user.profile[username]={
            "fullname":fullname,
            "phonenumber":phonenumber,
            "email":email,
            "address":address,
            "password":password,
            }
        print('\n')
        print("You have successfully updated your profile ")
        return user.profile
    