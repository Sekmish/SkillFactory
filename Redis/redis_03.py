import redis

r = redis.Redis(host='127.0.0.1', port=6379)

def add_friend_number():
    name = input('Введите имя друга: ')
    number = input('Введите номер телефона друга: ')
    r.set(name, number)
    print('Номер успешно сохранен')

def show_frienf_number():
    name = input('Введите имя друга: ')
    number = r.get(name)
    if number:
        print(f"Номер телефона друга {name}: {number.decode()}")
    else:
        print("Друг не найден")

def delete_friend_number():
    name = input('Введите имя другана: ')
    deleted = r.delete(name)
    if deleted:
        print("Номер успешно удален, не друг он больше")
    else:
        print('Друг не найден')

def main():
    while True:
        print("Выберите действие:")
        print("1. Записать номер друга")
        print("2. Показать номер друга")
        print("3. Удалить номер друга")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            add_friend_number()
        elif choice == "2":
            show_frienf_number()
        elif choice == "3":
            delete_friend_number()
        elif choice == "4":
            break
        else:
            print("Некорректный ввод - повтори")

if __name__ == "__main__":
    main()