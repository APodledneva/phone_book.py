phone_book = []
path = 'name.txt.'


def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def add_contact():
    print('Заполните форму: ')
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))
    print('\tКонтакт успешно добавлен')


def search_contact(phone_book):
    search = input('Введите ключевой элемент : ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)


def change_contact():
    search_ch = input('Введите ключевой элемента контакта : ')
    for contact in phone_book:
        for field in contact:
            if search_ch in field:
                print('Искомый контакт :', contact)
                replac_contact = int(input('Что вы хотите заменить:'
                                           '\n1 - имя '
                                           '\n2 - номер '
                                           '\n3 - комментарий '
                                           '\n4 - не менять'
                                           '\n'))
                match replac_contact:
                    case 1:
                        new_name = input('Введите новое Имя: ')
                        contact[0] = new_name
                        print(contact)
                    case 2:
                        new_num = input('Введите новый номер: ')
                        contact[1] = new_num
                        print(contact)
                    case 3:
                        new_com = input('Введите новый комментарий: ')
                        contact[2] = new_com
                    case 4:
                        break


def delete_contact():
    search_ch = input('Введите ключевой элемента контакта : ')
    for contact in phone_book:
        for field in contact:
            if search_ch in field:
                print('Искомый контакт :', contact)
                delet_con = int(input('Вы точно хотите удалить контакт?'
                                      '\n1-Да'
                                      '\n2-Нет'
                                      '\n \t '))
                match delet_con:
                    case 1:
                        phone_book.remove(contact)
                        print(f'Вы удалили контакт {contact}')
                    case 2:
                        break


def safe_file():
    def load_file(path: str) -> list:
        file = open(path, 'r', encoding='UTF-8')
        data = file.read()
        return data

    def save_file(path: str, data: str):
        file = open(path, 'w', encoding='UTF-8')
        file.write(data)
        file.close()

    file_to_save = []
    for i in phone_book:
        str_list = []
        for j in i:
            str_list.append(j)
        file_to_save.append(';'.join(str_list))

    save_file(path, '\n'.join(file_to_save))
