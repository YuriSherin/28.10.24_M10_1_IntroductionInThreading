import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    """Функция  должна вести запись слов "Какое-то слово № <номер слова по порядку>"
    в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
    В конце работы функции вывести строку "Завершилась запись в файл <название файла>"
    где:    word_count - количество записываемых слов,
            file_name - название файла, куда будут записываться слова."""

    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def main():
    t_st = datetime.now()   # запоминаем стартовое время
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    print(f'Работа главного потока: {datetime.now() - t_st} с.')

    t_st = datetime.now()   # запоминаем стартовое время
    """Создаем 4 вспомогательных потока"""
    thread1 = threading.Thread(target=write_words, args = (10, 'example5.txt'))
    thread2 = threading.Thread(target=write_words, args = (30, 'example6.txt'))
    thread3 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
    thread4 = threading.Thread(target=write_words, args = (100, 'example8.txt'))
    """Запускаем 4 вспомогательных потока в работы"""
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    """Приостанавливаем работу главного потока 
    до завершения работы вспомогательных потоков"""
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(f'Работа потоков: {datetime.now() - t_st} с.')





if __name__ == '__main__':
    main()

