# Задача №1: Сортировка слиянием

### Задание 

Реализовать алгоритм сортировки слиянием.

### Реализация

Сортировка слиянием (Merge Sort) - это алгоритм "разделяй и властвуй", который рекурсивно делит список на две половины до тех пор, пока не останутся списки длиной 1, которые затем последовательно сливаются в один отсортированный список. Основная идея - *разбить массив на части, рекурсивно отсортировать каждую и затем слить их обратно, сохраняя порядок*.

Так как рекурсии не слишком практичны: они используют много памяти и могут работать дольше итеративных алгоритмов, - было принято решение реализовывать сортировку без рекурсии. Вместо разделения массива на две части каждый раз (движение сверху вниз по дереву рекурсии), *список сразу делится на минимальные отсортированные блоки, затем они попарно сливаются в блоки побольше, пока размер блока не станет равным размеру самого списка* (движение снизу вверх по дереву рекурсии).
Функция `merge` позволяет объединять два отсортированных подмассива в один на месте, что снижает расходы на память.
Функция `merge_sort` сортирует массив in-place, не создавая дополнительных массивов, кроме необходимых для временного хранения частей.


### Анализ

Время O(n*log₂n)
Память O(n)