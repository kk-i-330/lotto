
import random, keyboard, os
print("Здравствуйте! Эта программа предназначена для проведения жеребьевки методом генерации случайных чисел.")
print("Давайте поиграем в лото!")
N = int(input("Введите количество бочонков: "))
sequence = [i for i in range(1, N+1)] ## создаем список бочонков 
sequence_new = [] ## создаем пустой список, в который далее будут помещаться вытянутые бочонки
for i in range(1, N+1):
    keyboard.wait('enter') ## при нажатии клавиши Enter происходит вытягивание бочонка
    print("Такие бочонки сейчас в мешке: ", sequence)
    C = random.choice(sequence) ## Возвращает случайный элемент заданной последовательности
    sequence_new.append(C) ## Добавляем в новый список вытянутый бочонок
    sequence.remove(C) ## Убираем из старого списка вытянутый бочонок
    print("Вытянули бочонки с номерами: ", sequence_new, "\n")
    print()
print("В мешке не осталось бочонков! Поздравляю победителей!", sequence)
os.system('pause')
