# -*- coding: utf-8 -*-

# def import_file(f, forma=1):
#     lst = []
#     with open(f, 'r') as f:
#         lst = f.readlines()
#     if forma == 1:
#         for el in lst:
#             with open('sotrudniki', 'a') as f:
#                 f.write(el)
#     else:
#         s = ''
#         for i, elem in enumerate(lst):
#             if elem != '\n':
#                 s += elem.strip() + ','
#             else:
#                 with open('sotrudniki', 'a') as f:
#                     f.write(s[::-1] + '\n')
#                 s = ''
#     print(f'Импорт {f} завершен')


def export_file(lst, n='all', forma=1):
    f_new = input('Введите имя файла для экспорта:') + '.txt'
    lst_ = []
    if n == 'all':
        lst_ = lst
    else:
        for i in range(int(n)):
            lst_.append(lst[i])
    if forma == 1:
        for el in lst_:
            with open(f_new, 'a') as f:
                f.write(el+ '\n')
    else:
        for elem in lst:
            el1 = elem.replace('*', '\n')
            with open(f_new, 'a') as f:
                f.write(el1 + '\n')
    print(f'Экспорт завершен. Файл {f_new} создан')


def append_rec(f):
    dl = count_rows(f)
    tn = dl-1
    print('Введите данные сотрудника:')
    stroka =str(tn) + '*' + input('Фамилия:') + '*' + input('Имя:') + '*' + input('Отчество:') + '*' + input(
        'Должность:') + '*' + input('Подразделение:') + '*'
    priz = input('Это руководитель? (+ если да, - если нет):')
    while priz not in ['-', '+']:
        priz = input('Введите признак руководителя (+ если да, - если нет):')
    okl = input('Оклад:')
    while not okl.isdigit():
        okl = input('Вы ввели не число. Введите корректный оклад:')
    stroka += priz + '*' + okl + '*' + '\n'
    with open(f, 'a') as f:
        f.write(stroka)
    print('Строка добавлена')


def show_all(lst_from_file, podr=''):
    for el in lst_from_file:
        if podr == '':
            s = el.replace('*', ' ')[:-1]
            print(s)
        elif podr in el:
            s = el.replace('*', ' ')[:-1]
            print(s)


def get_file(f, podr=''):
    s = []
    with open(f, 'r') as f:
        stroki_ = f.readlines()
    if podr == '':
        for el in stroki_:
            s.append(el[:-1])
    else:
        for el in stroki_:
            if podr in el:
                s.append(el[:-1])
    return s


def find_login(lst_from_file, x):
    stroka = []
    for el in lst_from_file:
        lst = el.split('*')
        if lst[0] == x:
            stroka = el.split('*')
    return stroka


def find_rec(lst_from_file, x):
    stroka = []
    for el in lst_from_file:
        if x in el:
            stroka = el
    return stroka


def del_rec(f, del_str):
    lst = get_file(f)
    with open(f, "w") as f:
        for line in lst:
            if line.strip("\n") != del_str:
                f.write(line+"\n")
    print(f'Запись "{del_str}" удалена')


