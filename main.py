# Задача 1: Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь 
# вводит номер строки, которую необходимо перенести из одного файла в другой.

# Задача 2: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также
# может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.



def input_surname():
    return input("Введите фамилию контакта: ").title()


def input_name():
    return input("Введите имя контакта: ").title()


def input_patronymic():
    return input("Введите отчество контакта: ").title()


def input_phone():
    return input("Введите телефон контакта: ")


def input_address():
    return input("Введите адрес(город) контакта: ").title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronymic} {phone} {address}\n"


def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(contact_str)


def create_list_contact():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    return contacts_str.rstrip().split("\n")

def print_contacts(cont_list=create_list_contact()):
    for n, contact in enumerate(cont_list, 1):
        print(n, contact)


def search_contact():
    print(
        "Возможные варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчество\n"
        "4. По телефону\n"
        "5. По адресу(город)"
    )
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный выбор!")
        var = input("Выберите вариант поиска: ")

    i_var = int(var) - 1

    search = input("Введите данные для поиска: ").title()

    contacts_list = create_list_contact()

    for str_contact in contacts_list:
        lst_contact = str_contact.split()
        if search in lst_contact[i_var]:
            print()
            print(str_contact)


def copy_contact():
    contacts_list = create_list_contact()
    
    print_contacts(contacts_list)
    print()

    num_contact_copy = int(input("Выберите номер контакта для копирования: ")) - 1
    while num_contact_copy not in range(len(contacts_list)):
        print("Некорректный выбор!")
        num_contact_copy = int(input("Выберите номер контакта для копирования: ")) - 1

    with open("phonebook_copy.txt", "a", encoding="utf-8") as file_copy:
        file_copy.write(f"{contacts_list[num_contact_copy]}\n")

    print("Контакт скопирован!")


def change_contact():
    contacts_list = create_list_contact()
    
    print_contacts(contacts_list)
    print()   

    num_contact_change = int(input("Выберите номер контакта для изменения: ")) - 1
    while num_contact_change not in range(len(contacts_list)):
        print("Некорректный выбор!")
        num_contact_change = int(input("Выберите номер контакта для изменения: ")) - 1

    print(
        "Варианты изменения контакта:\n"
        "1. Изменить фамилию\n"
        "2. Изменить имя\n"
        "3. Изменить отчество\n"
        "4. Изменить телефон\n"
        "5. Изменить адрес(город)")

    var = input("Выберите вариант изменения: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный выбор!")
        var = input("Выберите вариант изменения: ")
    i_var = int(var) - 1

    change_cont = input("Введите данные для изменения: ").title()
  
    lst_contact = contacts_list[num_contact_change].split()
    lst_contact[i_var] = change_cont
    contacts_list[num_contact_change] = " ".join(lst_contact)
        
    print("Данные изменены!")

    with open("phonebook.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(contacts_list))
        file.write("\n")


def delete_contact():
    contacts_list = create_list_contact()
    
    print_contacts(contacts_list)
    print()

    num_contact_del = int(input("Выберите номер контакта для удаления: ")) - 1
    while num_contact_del not in range(len(contacts_list)):
        print("Некорректный выбор!")
        num_contact_del = int(input("Выберите номер контакта для удаления: ")) - 1
    
    del contacts_list[num_contact_del]

    with open("phonebook.txt", "w", encoding="utf-8") as file_del:
        file_del.write("\n".join(contacts_list))
        file_del.write("\n")

    print("Контакт удален!")


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass

    var = 0
    while var != "7":
        print(
            "Возможные варианты:\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Изменить контакт\n"
            "6. Удалить контакт\n"
            "7. Выход"
        )
        print()
        var = input("Выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Некорректный выбор!")
            var = input("Выберите вариант действия: ")
        print()

        match var:
            case "1":
                add_contact()
            case "2":
                print(create_list_contact())
                print_contacts(create_list_contact())
            case "3":
                search_contact()
            case "4":
                copy_contact()
            case "5":
                change_contact()
            case "6":
                delete_contact()
            case "7":
                print("До свидания!")
        print()


if __name__ == "__main__":
    interface()
