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
            with open("groups/family.txt","r",encoding="utf=8") as file:
                for line in file:
                    counts += 1
            with open("groups/family.txt","a",encoding="utf=8") as file:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file.write(stringvalue + ")")
                file.write( name)
                file.write(r" - " + number)
                file.write("\n")
        if(group == 2):
            with open("groups/friends.txt","r",encoding="utf=8") as file:
                for line in file:
                    counts += 1
            with open("groups/friends.txt","a",encoding="utf=8") as file:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file.write(stringvalue + ")")
                file.write( name)
                file.write(r" - " + number)
                file.write("\n")
        if(group == 3):
            with open("groups/work.txt","r",encoding="utf=8") as file:
                for line in file:
                    counts += 1
            with open("groups/work.txt","a",encoding="utf=8") as file:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file.write(stringvalue + ")")
                file.write( name)
                file.write(r" - " + number)
                file.write("\n")
        if(group == 4):
            with open("groups/other.txt","r",encoding="utf=8") as file:
                for line in file:
                    counts += 1
            with open("groups/other.txt","a",encoding="utf=8") as file:
                name = input("Введите имя:")
                number = input("Введите номер:")
                stringvalue = str(counts)
                file.write(stringvalue + ")")
                file.write( name)
                file.write(r" - " + number)
                file.write("\n")
    
    if(choice == 2):
        
        

        



