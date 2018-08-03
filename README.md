# Ближайшие бары

## Для начала работы необходимо скачать файл с портала *data.mos.ru*\
***
Далее задется функция **def load_data**, которая возвращает информацию по барам *data*.
Чтобы найти бары с наибольшим и наименьшим колечеством сидячих мест, используем функции **get_biggest_bar** и **get_smallest_bar**, аргументами к которым передается возвращенная ранее *data*
Для поиска ближайшего к пользователю бара, используется функция **get_closest_bar** , но для того чтобы произвести этот рассчет, необходимы не только данные пользователя, но и функция которая будет пробегать по всем координатам баров и возвращать расстояния до пользователя. Для этого используется **get_distance**.

Функция **parse_args** использутся для разбора скачанной базы данных по барам из формата JSON. 
Для запуска необходимо заменить *parse_args()* на имя реального файла, например:
```python
data = load_data('bars.json')
```
Таким образом после запуска программы получаем следующие сообщния в консоли:
```bash
Самый вместительный бар: Спорт бар «Красная машина»
Бар с наименьшим количеством посадочных мест: Сушистор
Чтобы найти ближейший бар укажите Ваши координаты
Введите значение долготы:
```
Далее вводим значения своих координат и получаем информацию по ближайшему бару:
```bash
Чтобы найти ближейший бар укажите Ваши координаты
Введите значение долготы:37.4564874621
Введите значение широты:55.45687651354
Ближайший к Вам бар: Бар Виват
```


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
