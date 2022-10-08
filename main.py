# -*- coding: utf-8 -*-
import UI

print('Информационная система Штатное расписание')
UI.vhod()
# обработчик нажатия на клавишу 'Войти'
# def clicked():
# global username
# global password
# получаем имя пользователя и пароль
# username = str(username_entry.get())
# password = str(password_entry.get())
# check_logon(username, password)
# выводим в диалоговое окно введенные пользователем данные
# window.destroy()


# # главное окно приложения
# window = tkinter.Tk()
# # заголовок окна
# window.title('Авторизация')
# # размер окна
# window.geometry('450x230')
# # можно ли изменять размер окна - нет
# window.resizable(False, False)
#
# # кортежи и словари, содержащие настройки шрифтов и отступов
# font_header = ('Arial', 15)
# font_entry = ('Arial', 12)
# label_font = ('Arial', 11)
# base_padding = {'padx': 10, 'pady': 8}
# header_padding = {'padx': 10, 'pady': 12}
#
# # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# # для всех остальных виджетов настройки делаются также
# main_label = tkinter.Label(window, text='Авторизация', font=font_header, **header_padding)
# # помещаем виджет в окно по принципу один виджет под другим
# main_label.pack()
#
# # метка для поля ввода имени
# username_label = tkinter.Label(window, text='Имя пользователя', font=label_font, **base_padding)
# username_label.pack()
#
# # поле ввода имени
# username_entry = tkinter.Entry(window, bg='#fff', fg='#444', font=font_entry)
# username_entry.pack()
#
# # метка для поля ввода пароля
# password_label = tkinter.Label(window, text='Пароль', font=label_font, **base_padding)
# password_label.pack()
#
# # поле ввода пароля
# password_entry = tkinter.Entry(window, bg='#fff', fg='#444', font=font_entry)
# password_entry.pack()
#
# # кнопка отправки формы
# send_btn = tkinter.Button(window, text='Войти', command=clicked)
# send_btn.pack(**base_padding)
#
# # запускаем главный цикл окна
# window.mainloop()
