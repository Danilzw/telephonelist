import os

# Function to clear console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


#Home Page

while True:

    print("Добавить контакт", "|","Удалить контакт", "|","Вывести контакты", "|","Изменить контакт" ,"|","Закрыть программу","|")
    choice = int(input("                      Выберете(1,5):"))

# Menu Function
    if(choice == 5):
        break
    if(choice == 1):
        clear_console()
        print("\nСемья","|","Друзья","|","Работа","|","Другое","|","Назад","|")
        group = int(input("Выберете группу(1,5):"))
    #Add Function
        if(group == 5):
            clear_console()
        if(group == 1):
            counts = 0
            with open("groups/family.txt","r",encoding="utf=8") as file1:
                for line in file1:
                    counts += 1
            with open("groups/family.txt","a",encoding="utf=8") as file1:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file1.write(stringvalue + ")")
                file1.write( name)
                file1.write(r" - " + number + "\n")
           
                
        if(group == 2):
            counts = 0
            with open("groups/friends.txt","r",encoding="utf=8") as file2:
                for line in file2:
                    counts += 1
            with open("groups/friends.txt","a",encoding="utf=8") as file2:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file2.write(stringvalue + ")")
                file2.write( name)
                file2.write(r" - " + number + "\n")
               
            
        if(group == 3):
            counts = 0
            with open("groups/work.txt","r",encoding="utf=8") as file3:
                for line in file3:
                    counts += 1
            with open("groups/work.txt","a",encoding="utf=8") as file3:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file3.write(stringvalue + ")")
                file3.write( name)
                file3.write(r" - " + number + "\n")
                
            
        if(group == 4):
            counts = 0
            with open("groups/other.txt","r",encoding="utf=8") as file4:
                for line in file4:
                    counts += 1
            with open("groups/other.txt","a",encoding="utf=8") as file4:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file4.write(stringvalue + ")")
                file4.write( name)
                file4.write(r" - " + number + "\n")
                
            
    # Delete Function
    if(choice == 2):
        clear_console()
        print("\nСемья","|","Друзья","|","Работа","|","Другое","|","Назад","|")
        group = int(input("Выберете группу(1,5):"))

        if(group == 1):
            with open("groups/family.txt","r",encoding="utf-8") as file:
                print(file.read())
            arraytemp = []
            id = int(input("Кого хотите удалить?(id):"))
            with open("groups/family.txt","r",encoding="utf-8") as file2:
                for line in file2:
                    arraytemp.append(line)
            del arraytemp[id]
            with open("groups/family.txt","w",encoding="utf-8") as file:
                for i in arraytemp:
                    file.write(i)
        if(group == 2):
            with open("groups/friends.txt","r",encoding="utf-8") as file:
                print(file.read())
            arraytemp = []
            id = int(input("Кого хотите удалить?(id):"))
            with open("groups/friends.txt","r",encoding="utf-8") as file2:
                for line in file2:
                    arraytemp.append(line)
            del arraytemp[id]
            with open("groups/friends.txt","w",encoding="utf-8") as file:
                for i in arraytemp:
                    file.write(i)
        if(group == 3):
            with open("groups/work.txt","r",encoding="utf-8") as file:
                print(file.read())
            arraytemp = []
            id = int(input("Кого хотите удалить?(id):"))
            with open("groups/work.txt","r",encoding="utf-8") as file2:
                for line in file2:
                    arraytemp.append(line)
            del arraytemp[id]
            with open("groups/work.txt","w",encoding="utf-8") as file:
                for i in arraytemp:
                    file.write(i)
        if(group == 4):
            with open("groups/other.txt","r",encoding="utf-8") as file:
                print(file.read())
            arraytemp = []
            id = int(input("Кого хотите удалить?(id):"))
            with open("groups/other.txt","r",encoding="utf-8") as file2:
                for line in file2:
                    arraytemp.append(line)
            del arraytemp[id]
            with open("groups/other.txt","w",encoding="utf-8") as file:
                for i in arraytemp:
                    file.write(i)
        
    #Read Function
    if(choice == 3):
        clear_console()
        print("\nСемья","|","Друзья","|","Работа","|","Другое","|","Назад","|")
        group = int(input("Выберете группу(1,5):"))
        if(group == 1):
            with open("groups/family.txt","r",encoding="utf-8") as file:
                print(file.read())
        if(group == 2):
            with open("groups/friends.txt","r",encoding="utf-8") as file:
                print(file.read())
        if(group == 3):
            with open("groups/work.txt","r",encoding="utf-8") as file:
                print(file.read())
        if(group == 4):
            with open("groups/other.txt","r",encoding="utf-8") as file:
                print(file.read())
        
    #Change function
    if(choice == 4):
        clear_console()
        print("\nСемья","|","Друзья","|","Работа","|","Другое","|","Назад","|")
        group = int(input("Выберете группу(1,5):"))
        if(group == 1):
            with open("groups/family.txt","r",encoding="utf-8") as file:
                print(file.read())
            arraytemp = []
            id = int(input("Кого хотите изменить?(id):"))
            with open("groups/family.txt","r",encoding="utf-8") as file2:
                for line in file2:
                    arraytemp.append(line)
            newname = input("Введите имя:")
            newnumber = input("Введите номер:")
            arraytemp[id] = ((newname + " - " + newnumber))
            with open("groups/family.txt","w",encoding="utf-8") as file:
                  for i in arraytemp:
                      file.write(i)
            



        
        

        



