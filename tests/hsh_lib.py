import hashlib
import time

# Записываем в переменную время старта программы
time_start = time.time()

# Хешируем
data_hash = '   MikesoWeb  '
hash_pass = hashlib.md5(data_hash.strip().encode('utf-8')).hexdigest()

# Создаем файл pass.txt с методом append, который разрешает дозапись в файл,
# а если такой фал есть то переходим к след операции
record_file = open('pass.txt', 'a')
# записывае наш новый хеш и переходим на следующую строку
record_file.write(hash_pass + '\n')
# Закрываем файл
record_file.close()

# Записываем в переменную время окончания программы
time_finish = time.time()

print(f'Получите хеш: {hash_pass}')
# Получаем время выполнения программы
print(f'Время выполнения программы: {time_finish - time_start}')
