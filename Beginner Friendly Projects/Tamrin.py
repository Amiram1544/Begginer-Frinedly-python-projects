import datetime

def khoshamad():
    print ("*****************Salam*****************")
    print ('Be Dastyar shakhsi khodet khosh oomadi')
    zaman = datetime.datetime.now().strftime("%H:%M")
    name = input("esmet chie? ")
    print(f"{name} dar zaman {zaman} be system vared shod. ")
    return name

name = khoshamad() 

def menu():
    print ("yek gozine ra entekhab konid: ")
    print ("* 1. To-Do List *")
    print ("* 2. Mashin Hesab *")
    print ("* 3. Tarikh va Saat *")
    print ("* 4. Exit *")

while True:
    menu()
    choice = input("Az 1 - 4 gozineh mored nazar ra vared konid: ")

    if choice == '4' :
        print (f"Be omid didar {name}")
        break
    elif choice == '1' :
        tasks = []

        def add_task():
            task = input("Task khod ra ezafe konid: ")
            tasks.append(task)
            print(f"Task **{tasks}** ezafe shod ")

        def remove_task():
            view_task()
            shomare = int(input("Task mored nazar khod ra baraye hazf kardan entekhab konid: "))
            if 0<=shomare< len(tasks) :
                hazf = tasks.pop(shomare)
                print (f"Task **{hazf}** az list hazf shod. ")
            else :
                print(" adad mored nazar yaft nashod ")

        def view_task() :
            if not tasks:
                print (" List task haye shoma khali ast. ")

            else :
                print(" **your to do list** ")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

                

        def to_do_menu():
            while True:
                print("****** To-Do List ******")
                print (" 1. Add task ")
                print (" 2. Remove a task ")
                print (" 3. View tasks ")
                print (" 4. Exit to main menu ")

                choice = int(input(" chikar konam? "))

                if choice == 1 :
                    add_task()
           
                elif choice == 2 :
                    remove_task()

                elif choice == 3 :
                    view_task()

                elif choice == 4 :
                    break

                else : 
                    print ("invalid number ")

        to_do_menu()

        
    elif choice == '2' :
        def mashin_hesab():
            import math

        print ("****** Mashin Hesab ******")
        num1 = float(input("Adad aval khod ra vared konid. "))
        num2 = float (input("Adad dovom khod ra vared konid. "))
        operation = input("Chikaresh konam? (+ , - , * , / )")

        if operation == "+":
            javab = num1 + num2
        
        elif operation == "-":
            javab == num1 - num2

        elif operation == "*":
            javab= num1*num2

        elif operation == "/":
            if num2 == 0:
                print("** tagsim bar 0 mojaz nemibashad. **")
                break
            else:
                javab = num1 / num2

        else:
            print ("*** Mojaz nist ***")

        print (f"javab shoma baraye {num1} {operation} {num2} mosavi ast ba : {javab}")








         





    elif choice == '3':
        import datetime
        now = datetime.datetime.now()

        print ('****** Tarikh va Saat ******')

        print (now.strftime("Date: %Y-%m-%d"))
        print(now.strftime("Time: %H:%M:%S"))




    else :
        print ('****** Siktir ******')



    



    