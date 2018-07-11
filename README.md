# ChainStore by Maksym Skorupskyi for SECL Group
Python 3.7.0,
Django 2.0.7
_________________________________________________________________________________________________________

Task #1: - Complete

В этом задании Вам нужно создать проект управления сетью магазинов.

В нем должно быть несколько приложений - 
- места, 
- контактные лица, 
- магазины и 
- склады.

1) В местах должны быть сущности: 
- страны и 
- города. 
Страна и город должны иметь название, а также в городе должна быть указана страна.

2) В контактных лицах должны быть сущности контактных лиц, которые имеют: 
- имя, 
- фамилию, 
- пол, 
- дату рождения и 
- e-mail. 
Один e-mail не может быть у разных контактных лиц.

3) В магазинах должны быть сущности: 
- типа магазина и 
- самого магазина. 

Тип магазина имеет только название (может иметь значение одежда, еда, стройматериалы, супермаркет, и т.д.). 

Магазин имеет:
- тип магазина, 
- название, 
- владельца (только один)
- продавцов (>= 1) 
- склады (>=1)
- город, 
- адрес
- сайт (default=None)

Магазин может иметь только одного владельца (one-to-one), 
но может иметь много продавцов и складов (one-to-many). 
Магазин может не иметь сайт.

4) В складах должна быть сущность склада. 
Склад имеет: 
- название,
- город и 
- адрес.

Все модели нужно добавить в админку и заполнить ее данными (по не менее 10 записей на каждую модель).

_________________________________________________________________________________________________________

Task #2 - Complete

1. Нужно разобраться с HTTP (например тут http://ru.wikipedia.org/wiki/HTTP).

2. Нужно разобраться с основами HTML (например тут http://www.zvirec.com/html_book.php?id=1).

3. Сделать базовый шаблон с блоками: 
- title (заголовок документа), 
- хедер (верх страницы), 
- контент (средняя часть) и 
- футер (нижняя часть). 

Для этого шаблона можете создать папку в папке проекта, либо в главном приложении.

4. Для каждого приложения нужно создать файл urls.py 
и все правила для каждого приложения писать в свой urls.py. 
То же самое с папкой templates и шаблонами.

6. Для каждой модели создать две view-функции: 
- первая отображает список объектов, 
- вторая показывает полное описание объекта. 
Какие поля и как отображать - решаете сами. 
Для отображения списка используйте тег цикла {% for %} 
https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#for

7. В списках объектов сделать ссылки на страницы полного описания. Для того, чтобы генерировать ссылки, нужно использовать тег {% url 'urlname' arg1 args2 ... %} 
https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#url).

8. Добавить главную страницу с ссылками на страницы со списками объектов.

9. Все шаблоны страниц должны унаследовать главный шаблон и заполнять нужные блоки.

10. Если есть желание, то ознакомьтесь с Bootstrap http://getbootstrap.com/ и используйте его. 
(Как раздавать статику я показывал на одном из предыдущих занятий).

В результате получиться простенький сайт-каталог "сеть магазинов".

PS: для того, чтобы получить человеко-понятное отображение числового поля с choices, 
нужно использовать метод get_FOO_display() 

https://docs.djangoproject.com/en/1.7/ref/models/instances/#django.db.models.Model.get_FOO_display, 

например person.get_sex_display()
