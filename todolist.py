user_ip ='random' #define this as anything as declearation
data=[] #empty list 
def show_menu():
    print("-----TO DO MENU-----")
    print("1. Add a To Do Task")
    print("2. Remove Your Task")
    print("3. View Your Tasks ")
    print('4. Goodbye')
    print("-----END-----")
while user_ip != '4':
    show_menu()
    user_ip =input("\n \n Enter a Choice :")
    if user_ip == '1':
        task=input("Hello, What your is your Tasks ? \n")
        data.append(task);   #it add my items here
        print("Addded",task)

    elif user_ip == '2':
        task=input("What Task You Complete ? \n")
        if task in data:     # it check weather the task is present in the data or not
            data.remove(task)
            print(task ,"Is Marked as Done\n")

        else:
            print("Sorry ths Task is not exist !\n")

    elif user_ip == '3':
        print("Your To Do Tasks are :")
        for task in data:
            print(task)
           

    elif user_ip == '4':
        print("Goodbye")
        

    else:
        print("Plese enter one of 1, 2, 3 or 4 ")
        

