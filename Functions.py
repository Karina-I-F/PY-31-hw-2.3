documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
    {'type': 'insurance', 'number': '25894'}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '25894'],
    '3': []
}


def get_full_name_by_number(doc_list):
    """
    Принимает номер документа и выводит имя
    """
    number = input('Введите номер документа: ')
    for key in doc_list:
        if key.get('number') == number:
            print(key.get('name'))
            break
    else:
        print('Документ не найден. Проверьте данные.')


def get_shelf_by_number(direct_dict):
    """
    Спрашивает номер документа и показывает номер полки
    """
    number = input('Введите номер документа: ')
    for key, value in direct_dict.items():
        if number in value:
            print(f'Документ находится на {key} полке.')
            break
    else:
        print('Документ не найден. Проверьте данные.')


def print_list(doc_list):
    """
    Выводит список всех документов
    """
    for line in doc_list:
        try:
            line['name']
        except KeyError:
            print('У', line['type'], 'под номером', line['number'],
                  'отсутствует присвоенное имя владельца.')
        else:
            print(line['type'], '-', line['number'], '-', line['name'])

def print_name(doc_list): # Новая функция для ДЗ
    """
    Выведет имена всех владельцев документов
    """
    for line in doc_list:
        try:
            line['name']
        except KeyError:
            print('У документа под номером', line['number'],
                  'отсутствует присвоенное имя владельца.')
        else:
            print(line['name'])

def add_doc(doc_list, direct_dict):
    """
    Спрашивает тип, номер документа, имя владельца и номер полки,
    затем добаляет новый документ
    """
    view = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите имя владельца: ')
    shelfs = list(direct_dict.keys())
    shelf = input(f'Введите номер полки {shelfs} для хранения документа: ')
    if shelf in shelfs:
        new_doc = {'type': view, 'number': number, 'name': name}
        doc_list.append(new_doc)
        direct_dict[shelf].append(number)
        print(f'Добавлено на полку {shelf}')
    else:
        print(f'Данной полки не существует. Попробуйте снова {shelfs}')


def delete_doc(doc_list, direct_dict):
    """
    Спросит номер документа и удалит его из каталога и из перечня полок
    """
    number = input('Введите номер документа: ')
    i = 0
    for key in doc_list:
        if key.get('number') == number:
            del doc_list[i]
            break
        i += 1
    for key, value in direct_dict.items():
        if number in value:
            direct_dict[key].remove(number)
            print('Документ успешно удалён из каталога.')
            break
    else:
        print('Документ не найден. Проверьте данные.')


def move_doc(direct_dict):
    """
    Спросит номер документа и целевую полку
    и переместит его с текущей полки на целевую
    """
    number = input('Введите номер документа: ')
    shelf = input('Введите номер полки, на которую хотите переместить документ: ')
    shelfs = list(direct_dict.keys())
    if shelf in shelfs:
        if number in direct_dict[shelf]:
            print('Документ уже находится на данной полке.')
        else:
            for key, value in direct_dict.items():
                if number in value:
                    direct_dict[key].remove(number)
                    direct_dict[shelf] = [number]
                    print(f'Документ успешно перемещён на {shelf} полку.')
                    break
            else:
                print('Документ не найден. Проверьте данные.')
    else:
        print(f'Данной полки не существует. Попробуйте снова {shelfs}')


def add_shelf(direct_dict):
    """
    Спросит номер новой полки и добавит ее в перечень
    """
    shelf = input('Введите номер полки, которую хотите добавить ')
    if shelf not in direct_dict.keys():
        direct_dict[shelf] = []
        print(f'Полка №{shelf} успешно создана')
    else:
        print('Данная полка уже существует')


def databank():
    """
    Выводит перечень команд для пользователя
    """
    while True:
        choice_str = input('\n\
        ***\n\n\
        Введите команду:\n\n\
        fn – команда full name\n\
        спросит номер документа и выведет имя человека, которому он принадлежит;\n\n\
        s – команда shelf\n\
        спросит номер документа и выведет номер полки, на которой он находится;\n\n\
        pl – команда print list\n\
        выведет список всех документов в формате\n\
        "passport - 2207 876234 - Василий Гупкин";\n\n\
        pn – команда print name\n\
        выведет имена всех владельцев документов;\n\n\
        ad – команда add document\n\
        добавит новый документ в каталог и в перечень полок;\n\n\
        dd – команда delete document\n\
        спросит номер документа и удалит его из каталога и из перечня полок;\n\n\
        md – команда move document\n\
        спросит номер документа и полку и переместит его с текущей полки на нужную;\n\n\
        as – команда add shelf\n\
        спросит номер новой полки и добавит ее в перечень;\n\n\
        q - команда quit\n\
        завершение программы.\n\n\
        -> ')
        choice = choice_str.lower()
        if choice == 'fn':
            get_full_name_by_number(documents)
        elif choice == 's':
            get_shelf_by_number(directories)
        elif choice == 'pl':
            print_list(documents)
        elif choice == 'pn': # Новая функция для ДЗ
            print_name(documents)
        elif choice == 'ad':
            add_doc(documents, directories)
        elif choice == 'dd':
            delete_doc(documents, directories)
        elif choice == 'md':
            move_doc(directories)
        elif choice == 'as':
            add_shelf(directories)
        elif choice == 'q':
            print('Выход выполнен.')
            break
        else:
            print('Введены не верные данные. ' 
            'Требуется ввести первые буквы команды на литиннице.')


databank()