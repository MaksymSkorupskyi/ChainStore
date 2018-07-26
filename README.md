# ChainStore by Maksym Skorupskyi for SECL Group
Python 3.7.0,
Django 2.0.7
_________________________________________________________________________________________________________

Task #1: - Complete (4/4)

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

Task #2 - Complete (10/10)

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

PS: для того, чтобы получить понятное отображение числового поля с choices, 
нужно использовать метод get_FOO_display() 

https://docs.djangoproject.com/en/1.7/ref/models/instances/#django.db.models.Model.get_FOO_display, 

например person.get_sex_display()

_________________________________________________________________________________________________________

Task #3 - in progress (5/7)

1. Написать и подключить Middleware, который будет сохранять: 
- дату, 
- время, 
- метод запроса (GET, POST и т.д.), 
- URL (с доменом и GET-параметрами) запросов и 
- время генерации ответа с точностью до 0.0001 секунды 
в файл 'projectname/requests.log'. 
Каждый запрос в отдельную строку.

2. Написать и подключить контекст процессор, в котором будет имя разработчика (т.е. Ваше имя) и использовать этот контекст в футере страниц.

3. Написать страницы для создания и редактирования всех своих моделей в проекте (используя ModelForm). 
- Для редактирования магазина и типа магазина используйте CBV на базе TemplateView. 
- Для склада и контактного лица обычные функции. 
- Для Города и страны -- CBV на базе UpdateView. 
После удачной обработки формы нужно создать сообщение используя messages и сделать redirect.

4. На страницах со списком объектов добавить кнопку или ccылку "Добавить" и возле каждого элемента в списке добавить ссылку "Редактировать". 
Ссылки должны направлять на страницы, которые описаны в п.3.

5. Для вывода сообщений messages написать inclusion_tag для шаблона, который будет их выводить. Тег должен иметь один параметр, который по умолчанию будет иметь значение True. 
Если передать False, тогда сообщения не должны выводится.

6. Поля форм нужно выводить вручную отдельно. 
Для отображения ошибок использовать свой тег для шаблона, который будет принимать объект со списком ошибок и выводить эти ошибки в удобно-читаемом виде.

7. Написать фильтр для шаблонов, который будет получать на вход объект магазина, а на выходе возвращать список объектов продавцов, сортированных по имени по алфавиту. 
Использовать этот фильтр на странице вывода информации о конкретном магазине. 
(Сортировку нужно сделать после того, как получите список объектов продавцов)

_________________________________________________________________________________________________________

Task #4 - incomplete (0/6)

1. Сделать сайт многоязычным (2-3 языка). Нужно локализировать все фразы в коде и шаблонах. Можно весь перевод держать в папке locale, которую создать в папке проекта и прописать в settings.LOCALE_PATHS, либо для каждой аппликации отдельно. Также нужно добавить переключалку языка, которая будет отображаться на всех страницах сайта.


2. Используя систему полномочий закрыть страницы редактирования и создания объектов -- эти страницы должны работать только для пользователей, которые имеют соответствующие полномочия для моделей объектов (change для редактирования и add для создания). Также нужно убирать ссылки на страницы, для которых у пользователя нету полномочий.


3. Добавить кнопку "удалить" на странице редактирования объекта. Кнопка должна отображаться и работать только тогда, когда в пользователя есть полномочие delete для модели данного объекта. При удалении должно быть подтверждение удаления (можно использовать готовые CBV).


4. Для модели магазина добавить поле с номером версии (правки), которое по умолчанию 0. При каждом изменении магазин с помощью сигналов версия должна увеличиваться на единицу. Данное поле не должно отображаться в формах (и в админке). 
Также добавить отображение номера версии на страницу просмотра магазина.


5. Используя FlatPages сделать две страницы: "о проекте" и "правила использования". В футере вывести список ссылок на эти страницы используя темплейт-теги модуля FlatPages.


6. Настроить LocMemCache кеш, кешировать главную страницу на 15 минут и футер (в базовом шаблоне) на 3 часа.

_________________________________________________________________________________________________________