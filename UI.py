# -*- coding: utf-8 -*-
# from tkinter.filedialog import askopenfilename
import model


def menu_all():
    while True:
        print(f'1 - Показать всех сотрудников\n'  # model.show_all(f, podr='')
              f'2 - Показать сотрудников подразделения\n'
              f'3 - Экспорт списка сотрудников в файл\n'  # model.export_file(n='all', forma=1)
              f'4 - Добавить сотрудника\n'  # model.append_rec(f)
              f'5 - Найти сотрудника\n'  # model.find_rec(lst_from_file, x)
              f'6 - Удалить сотрудника\n'  # model.del_rec(str_record, del_param)
              f'0 - Выход из программы\n')
        n = int(input(f'Введите номер действия:'))
        if n == 0:
            print('До свидания. Хорошего дня!')
            break
        elif n == 1:
            model.show_all(model.get_file('sotrudniki'))
        elif n == 2:
            model.show_all(model.get_file('sotrudniki', input('Введите подразделение:')))
        elif n == 3:
            depart = input('Введите подразделение для экспорта (для вывода всех записей нажмите ввод):')
            count_f = len(model.get_file('sotrudniki', podr))
            s = input(f'Введите число строк для экспорта от 1 до {count_f} (по умолчанию экспортируются все '
                      f'строки)')
            form1 = int(input(f'Выберите формат экспорта (1 - в строку, 2 - в столбик):'))
            if s == '':
                cnt_str = count_f
            else:
                cnt_str = int(s)
            model.export_file(model.get_file('sotrudniki', depart), cnt_str, form1)
        elif n == 4:  # Добавить сотрудника
            model.append_rec('sotrudniki')
        elif n == 5:  # Найти сотрудника
            found = model.find_rec(model.get_file('sotrudniki'),
                                   input('Введите Фамилию:') + '*' + input('Введите Имя:') + '*' + input(
                                       'Введите Отчество:'))
            if found == []:
                print('Такой сотрудник не найден.')
            else:
                model.show_all(model.get_file('sotrudniki'), found)
        elif n == 6:  # Удалить сотрудника
            poisk = input('Введите Фамилию сотрудника:') + '*' + input('Введите Имя сотрудника:') + '*' + input(
                'Введите Отчество сотрудника:')
            found = model.find_rec(model.get_file('sotrudniki'), poisk)
            if found == []:
                print('Такой сотрудник не найден.')
            else:
                print(f'Сотрудник найден:{found}')
                print(f'Точно хотите удалить:{found}?\n'
                      f'Введите 1 - для удаления или любой символ - для отказа\n')
                p = input('Ваше решение:')
                if p == '1':
                    model.del_rec('sotrudniki', found)
                    print('Запись удалена.')
                else:
                    print('Вы отменили удаление.')


def menu_ruk_otd(podr):
    while True:
        print(f'1 - Показать сотрудников подразделения\n'  # model.show_all(f, podr='')
              f'2 - Экспорт сотрудников подразделения в файл\n'  # model.export_file(n='all', forma=1)
              f'3 - Найти сотрудника\n'  # model.find_rec(lst_from_file, x)
              f'0 - Выход из программы\n')
        n = int(input(f'Введите номер действия:'))
        if n == 0:
            print('Работа программы завершена.')
            break
        elif n == 1:
            model.show_all(model.get_file('sotrudniki', podr))
        elif n == 2:
            count_f = len(model.get_file('sotrudniki', podr))
            s = input(f'Введите число строк для экспорта от 1 до {count_f} (по умолчанию экспортируются все '
                      f'строки)')
            form1 = int(input(f'Выберите формат экспорта (1 - в строку, 2 - в столбик):'))
            if s == '':
                cnt_str = count_f
            else:
                cnt_str = int(s)
            model.export_file(model.get_file('sotrudniki', podr), cnt_str, form1)
        elif n == 3:
            found = model.find_rec(model.get_file('sotrudniki', podr),
                                   input('Введите Фамилию:') + '*' + input('Введите Имя:') + '*' + input(
                                       'Введите Отчество:'))
            if found == []:
                print('Такой сотрудник не найден.')
            else:
                model.show_all(model.get_file('sotrudniki', podr), found)


def check_logon(x='', y=''):
    lst_ = []
    lst_ = model.find_login(model.get_file('users'), x)
    if lst_ == []:
        print('Неверный логин или пароль!')
        return '1'
    else:
        if y == lst_[1]:
            if lst_[2] == 'all':
                menu_all()
                return '0'
            elif lst_[2] == 'ruk_otd':
                menu_ruk_otd(lst_[3])
                return '0'
            else:
                print('Доступ не назначен. Обратитесь к администратору')
                return '1'
        else:
            print('Неверный пароль!')
            return '1'


def vhod():
    username = ''
    password = ''
    n = '1'
    while n != '0':
        username = input('Введите логин:')
        password = input('Введите пароль:')
        if username == '' or password == '':
            n = input('Логин или Пароль пустые.\nПопробовать снова - 1\nВыход - 0\nВведите свой выбор:')
            if n == '0':
                print('Работа программы завершена.')
                break
        else:
            n = check_logon(username, password)
