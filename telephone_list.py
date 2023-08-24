import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


#Home Page

while True:

    print("Добавить контакт", "|","Удалить контакт", "|","Вывести контакты", "|","Изменить контакт" ,"|","Закрыть программу","|")
    choice = int(input("                      Выберете(1,5):"))
    if(choice == 5):
        break
    if(choice == 1):
        clear_console()
        print("\nСемья","|","Друзья","|","Работа","|","Другое","|","Назад","|")
        group = int(input("Выберете группу(1,5):"))

        if(group == 5):
            clear_console()
        if(group == 1):
            with open("groups/family.txt","a",encoding="utf=8") as file:
                name = input("Введите имя:")
                number = input("Введите номер:")
                file.write("\n" + name)
                file.write(r" - " + number)

        



