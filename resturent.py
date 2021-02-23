class Manager:
     def takingOrder(self): 
          print("please place your order sir")
          o1=(input("First order : "))
          o2=(input("second order : "))
          o3=(input("third order : "))
          
          print(f"your orders are :\n{o1}\n{o2}\n{o3}\nThanks for ordering")

a = Manager()
a.takingOrder()
     
