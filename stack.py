data = []

def add(a):
    global data
    data.insert(0,a)

def pop():
    delete = data.pop(0)
    print(f"{delete} is removed.")

def view():
    for i in data: 
     print(f"|{i}|")
    
while True:
    choice = input("1.Add\n2.Pop\n3.View\n4.Exit\nEnter your choice:").lower()
    if choice == "1" or choice == "add":
        if len(data) == 3:
          print("*****Stack Is Full*****")

        else:
            add_value = add(input("Enter the number: "))

    elif choice == "2" or choice == "pop":
        if len(data) == 0:
            print("*****Stack Is Empty*****")
        
        else:
            pop()
            
    elif choice == "3" or choice == "view":
        if len(data) == 0:
            print("*****Stack Is Empty*****")

        else:
            view()

    elif choice == "4" or choice == "exit":
        print("Thank You!")
        break
    
    else:
        print("Invalid Input")
        continue


