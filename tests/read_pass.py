# импотрируем библиотеку для работы
import hashlib

# зашифровываем в 16-ти ричном формате пароль pass
h = hashlib.md5(b'pass').hexdigest()

count = 0     # создаем счетчик
while count < 3:   # пока count не равно трем, выполнять условие

    # Просим пользователя ввести пароль
    inp = input("Enter the password: ")  # Вводим  пароль pass
    # зашифровываем ввод пользователя
    p = hashlib.md5(inp.encode('utf-8')).hexdigest()
    count += 1  # каждую итерацию увеличиваем счетчик на один
    if p == h:  # если хеш пользователя и хеш в базе равны
        print('True')
    else:      # если хеш пользователя и хеш в базе равны
        print('False')

print(f'Вы ввели пароль {count} раза не правильно!')
print("Программа завершена!")