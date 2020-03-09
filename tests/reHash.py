# импотрируем библиотеки для работы
import hashlib
import time
# объявляем переменную-счетчик
count = 0
# откуда читать хеш
text_md5 = open(r'C:\Users\z\PycharmProjects\tests\pass.txt', 'r', encoding='utf-8')
# cчитываем из файла результат в  переменную
tm5 = text_md5.read()
# база с паролями, открываем файл в режиме чтения с кодировкай utf-8
file_dict = open(r'C:\Users\z\PycharmProjects\tests\base.txt', 'r', encoding='utf-8')
# cчитываем из файла все строки  переменную
fd = file_dict.readlines()
# записываем время старта программы
time_start = time.time()
# обрабатываем по строчно файл базы с паролями
for password in fd:
    # записываем в переменную результат выполнения функции кодирования
    hash_object = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    # переменная count ри каждом проходе увеличивается на еденицу
    count += 1

    # если результат цикла равен нашему хешу
    if hash_object == tm5:
        print(f'Пароль найден - {password} за количество попыток {count}')
        # выходим из программы
        break
    # иначе если результат цикла НЕ равен нашему хешу
    elif hash_object != tm5:
        # оператор-заглушка, равноценный отсутствию операции.
        pass
# записываем время окончания программы
time_finish = time.time()
# вычитаем время чтобы узнать сколько времени работала программа
time_work = time_finish - time_start
print(f'Время работы программы: {time_work}')
