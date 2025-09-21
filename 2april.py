#make a project for inventory system 
#wap to print square of 1 to 10 number in the form of  disctionay 
# for i in range (1,11,1):
#     print(i,":",i**2)
    #wap to find a cube of 11 to 20
# for i in range (11,21,1):
#     print(i,":",i**3)    
    #wap to enter fruits name with its qunatity from user in the form of disctionary
    # n=int(input("enter the quantity"))
    # d={}
    # for i in range(0,n,1):
    #     k=int(input("enter fruits name"))
    #     v=input("enter quantity")
    #     d.update({k:v})
    #     print(d)
#     n = int(input("Enter the quantity of different fruits: "))
# d = {}

# for i in range(n):
#     k = input("Enter fruit name: ")  
#     v = input("Enter quantity: ")   
#     d[k] = v

# print(d)
# inventory = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory.append([name, quantity, price])
    print("Item added.")

def view_inventory():
    print("\nInventory:")
    for item in inventory:
        print(f"{item[0]} - Quantity: {item[1]}, Price: {item[2]}")

def main():
    while True:
        choice = input("\n1. Add Item\n2. View Inventory\n3. Exit\nChoose: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
