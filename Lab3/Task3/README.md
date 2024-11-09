# Задача №3: Алгоритм сортировки "Scarecrow Sort"

## Описание задачи
Необходимо проверить, возможно ли отсортировать список с шагом delta.
## Структура кода
Код состоит из двух основных частей: реализации алгоритма сортировки и тестов для проверки корректности работы алгоритма. Сортировка проверяет возможность корректной сортировки с шагом `delta` и выполняет сортировку, если это возможно.

### Папка `src`
Папка с исходным кодом.

#### Файл `ScarecrowSort.py`

1. **Функция `scarecrow_sort_checking_indexes`**

   - **Параметры**:
     - `lst` (тип: `List[int]`) — список целых чисел для сортировки.
     - `delta` (тип: `int`) — шаг, с которым элементы могут перемещаться (индекс будет перемещаться на несколько позиций, кратных `delta`).

   - **Возвращаемое значение**:
     - `bool`: `True`, если сортировка возможна с данным шагом `delta`, иначе `False`.

   - **Описание**:
     - Сортирует список и сохраняет его как эталон.
     - Создает структуру данных для отслеживания индексов элементов в исходном списке.
     - Для каждого элемента в отсортированном списке проверяет, можно ли перенести его на нужную позицию с шагом `delta`. Если для какого-то элемента это невозможно, функция возвращает `False`.
     - Если все элементы могут быть правильно перемещены, возвращается `True`.

2. **Функция `scarecrow_sort_real_sorting`**

   - **Параметры**:
     - `lst` (тип: `List[int]`) — список целых чисел для сортировки.
     - `delta` (тип: `int`) — шаг для сортировки.

   - **Возвращаемое значение**:
     - `bool`: `True`, если список отсортирован, иначе `False`.

   - **Описание**:
     - Реализует саму сортировку с использованием шага `delta`. Для каждого индекса начиная с `delta` и до конца списка, если элемент больше элемента, расположенного на расстоянии `delta`, выполняется обмен значениями.
     - Сортировка продолжается, пока не будет достигнут нужный порядок элементов.
     - В конце функция сравнивает отсортированный список с результатом сортировки, чтобы убедиться в правильности результата.

3. **Функция `main`**

   - **Описание**:
     - Считывает данные (список и шаг `delta`) с помощью функции `read()`.
     - Проверяет, возможно ли отсортировать список с данным шагом с помощью функции `scarecrow_sort_checking_indexes`.
     - Если сортировка возможна, выполняет её с помощью функции `scarecrow_sort_real_sorting` и записывает результат в файл с помощью функции `write()`.
     - Если сортировка невозможна, выводится сообщение "NO".

4. **Запуск программы**
   - Блок `if __name__ == "__main__":` вызывает функцию `main()` для выполнения программы.

### Папка `tests`
Папка с тестами.

#### Файл `ScarecrowSort_test.py`

1. **Функция `test_first_example`**

   - **Описание**:
     - Тестирует алгоритм на примере списка `[2, 1, 3]` с шагом `2`.
     - Ожидаемый результат — сортировка невозможна, возвращает `False` для обеих функций `scarecrow_sort_checking_indexes` и `scarecrow_sort_real_sorting`.

2. **Функция `test_second_example`**

   - **Описание**:
     - Тестирует алгоритм на примере списка `[1, 5, 3, 4, 1]` с шагом `3`.
     - Ожидаемый результат — сортировка возможна, возвращает `True` для обеих функций.

3. **Функция `test_same`**

   - **Описание**:
     - Тестирует алгоритм на примере списка с одинаковыми элементами `[1, 1, 1, 1, 1, 1]` с шагом `3`.
     - Ожидаемый результат — сортировка возможна, возвращает `True` для обеих функций.

4. **Функция `test_simple_delta`**

   - **Описание**:
     - Тестирует алгоритм на случайных данных с шагом `1`.
     - Ожидаемый результат — сортировка возможна для всех случайных данных, возвращает `True` для обеих функций.

5. **Функция `test_time`**

   - **Описание**:
     - Проверяет производительность решения на больших входных данных.
     - Измеряет время выполнения функции и проверяет, что оно не превышает 2 секунд.

### Папка `txtf`
Папка с входными и выходными файлами.

#### Входные данные (`input.txt`)
Содержат список элементов для сортировки, а также шаг `delta`, через пробел.

#### Выходные данные (`output.txt`)
Содержат строку "YES", если сортировка возможна, или "NO" в случае невозможности сортировки.

## Запуск программы и тестов

### Решение

1. Перейдите в папку с решением задачи:
```bash
cd ITMOalgorithms/Lab3/Task2/
```

2. Исходные данные находятся в папке `txtf` в файле `input.txt`. Чтобы открыть его в текстовом редакторе:
```bash
notepad txtf/input.txt
```

3. Запустите программу:
```bash
python src/ScarecrowSort.py
```

4. Результаты будут записаны в `output.txt`. Чтобы открыть его в текстовом редакторе:
```bash
notepad txtf/output.txt
```

### Тестирование

1. Запустите тесты с помощью `pytest`:
```bash
pytest tests/ScarecrowSort_test.py
```
