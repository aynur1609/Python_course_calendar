import bcrypt
import sys
from Backend import Backend
from User import User
from colorama import Fore


# class Login:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.users = {}
#
#     def create_user(self):
#         if self.username in self.users:
#             print("Этот пользователь уже существует.")
#         else:
#             self.users[self.username] = self.password
#             print("Пользователь успешно создан.")
#
#     def authenticate_user(self):
#         if self.username in self.users and self.users[self.username] == self.password:
#             print("Успешная аутентификация.")
#         else:
#             print("Ошибка аутентификации.")
#
#
# login = Login(input("Введите имя пользователя: "), input("Введите пароль: "))
# login.create_user()
# login.authenticate_user()

class Interface:
    user = None
    state = "start"
    backend = Backend()
    backend.load_data()

    @staticmethod
    def start():
        menu = input(Fore.GREEN + """
        0)Войти в аккаунт
        1)Создать нового пользователя
        2)Завершить работу
        """)
        if menu == "0":
            Interface.enter()
        elif menu == "1":
            Interface.create_new_user()
        elif menu == "2":
            Interface.finish()

    def read(e):
        menu = input(Fore.GREEN + """
        0)Завершение работы
        1)Создание события
        2)Добавление пользователя
        3)Удаление пользователя
        3)Удаление события
        4)Просмотр всех событий
        """)
        if menu == "0":
            Interface.finish()
        elif menu == "1":
            pass


    @staticmethod
    def enter():
        login = input(Fore.GREEN + "Введите свой логин: ")
        user_exists = False
        for user in Interface.backend.get_users():
            if user.get_name() == login:
                user_exists = True
                password = input(Fore.GREEN + "Введите пароль: ")
                print(Fore.YELLOW + f"Введенный пароль: {password}")
                print(Fore.YELLOW + f"Хэш: {user.get_password()}")
                if user.check_password(password):
                    print(Fore.LIGHTBLUE_EX + "Welcome")
                else:
                    print(Fore.RED + "Логин или пароль неверный,введите заново")
                    Interface.start()
        if not user_exists:
            print(Fore.RED + "Пользователя не существует")
            Interface.enter()

    @staticmethod
    def get_user_by_login(login):
        users = Interface.backend.get_users()
        for user_obj in users:
            if user_obj.get_name() == login:
                return user_obj
        return None

    @staticmethod
    def create_event():
        pass

    @staticmethod
    def add_users_event():
        pass



    @staticmethod
    def remove_event():
        pass

    @staticmethod
    def view_events():
        pass

    @staticmethod
    def create_new_user():
        new_user = User.create_user()
        Interface.backend.add_users(new_user)
        Interface.user = new_user
        Interface.backend.save_data()
        print(Fore.GREEN + f"Новый профиль: {new_user}")
        i = input(Fore.GREEN + """
        0)Завершить работу
        1)Войти в существующий аккаунт
        """)
        if i == "0":
            Interface.finish()
        elif i == "1":
            Interface.enter()

    @staticmethod
    def request():
        pass

    @staticmethod
    def finish():
        print(Fore.GREEN + "Завершение работы.")
        sys.exit(0)


Interface.start()
print(Interface.backend.get_users())



