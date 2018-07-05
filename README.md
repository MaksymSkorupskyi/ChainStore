# ChainStore by Maksym Skorupskyi for SECL Group
Python 3.7.0

Django 2.0.7


Task:

В этом задании Вам нужно создать проект управления сетью магазинов.

В нем должно быть несколько приложений - 
- места, 
- контактные лица, 
- магазины и 
- склады. (4 шт.)

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
