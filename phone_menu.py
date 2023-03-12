menu = str('Главное меню: \n '
           '\t1. Открыть файл\n '
           '\t2. Сохранить файл\n '
           '\t3. Показать все контакты\n'
           '\t4. Создать контакт\n '
           '\t5. Изменить контакт\n '
           '\t6. Найти контакт\n '
           '\t7. Удалить контакт\n '
           '\t8. Выход')

print(menu)

from function_phone import *

while True:
    print('\nДля просмотра меню введите 0')
    number = int(input('Введите пункт меню: '))

    match number:
        case 0:
            print(menu)
        case 1:
            open_file(path)
            print('\nФайл успешно загружен')
        case 2:
            safe_file()
            print('Файл сохранен')
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            change_contact()
        case 6:
            search_contact(phone_book)
        case 7:
            delete_contact()
        case 8:
            print('Приходите еще ')
            break
