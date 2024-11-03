# Задача №4: Бинарный поиск

### Задание 

Реализовать алгоритм бинарного поиска

### Реализация

Бинарный поиск — это алгоритм поиска элемента в отсортированном списке. Он работает по принципу "разделяй и властвуй", на каждом шаге деля список пополам и проверяя, находится ли искомый элемент в левой или правой части.
Чтобы быстро выводить индекс элемента в неотсортированном списке, мы сортируем не сами элементы, а их индексы: индекс i является больше индекса j, если lst[i] больше lst[j]. Т.е. на позиции i хранится значение позиции в неотсортированном массиве, где стоял элемент, который в отсортированном массиве имеет индекс i.
Вместо рекурсии опять же использовался итеративный алгоритм, где роль разделения массива на две части играют два указателя, показывающие, с какой частью списка мы работаем. Алгоритм итеративного бинарного поиска начинается с установки начального значения границ поиска (left = 0, right = n-1). Затем определяется позиция mid как среднее между left и right. Элемент на позиции mid сравнивается с целевым значением. Если они равны, поиск завершен успешно. В противном случае, если элемент меньше целевого, left увеличивается, а если больше, right уменьшается. Процесс продолжается до тех пор, пока left не станет больше right, указывая на отсутствие элемента.


### Анализ

Время O(log₂n)
Память O(1)