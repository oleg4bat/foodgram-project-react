[![Django-app workflow](https://github.com/oleg4bat/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/oleg4bat/foodgram-project-react/actions/workflows/main.yml)

### [Что это за Foodgram?](http://ovz8.j66017249.pvl9n.vps.myjino.ru/):smiley_cat: 
Foodgram - это онлайн-сервис + API (DRF), благодаря которому пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Как запустить? :space_invader:
Проект можно запустить, используя Docker для этого:

Клонировать репозиторий:

```
git clone git@github.com:oleg4bat/foodgram-project-react.git
```
Перейти в папку /infra

```
cd infra
```

Cоздать и запустить контейнеры:

```
docker compose up -d --build
```

Для полноценного функционирования проекта необходимо выполнить миграции и собрать статику:
- Зайти в контейнер web

```
docker exec -it <CONTAINER ID> bash
```

- Выполнить миграции и сollectstatic в папке с manage.py

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```


### Пример взаимодействия с API :old_key:
После запуска проекта для получения полного доступа к интерфейсу необходимо: 

1. Создать нового пользователя, отправив POST запрос на эндпоинт http://localhost:8000/api/users/
с именем пользователя и почтой в формате:

```
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "Qwerty123"
}
```

2. Получить auth-токен для авторизации, отправив POST запрос в формате: 
```
{
"password": "string",
"email": "string"
}
```
на эндпоинт http://127.0.0.1:8000/api/v1/auth/token/login/

Токен из строки "token" необходимо отправлять в headers запроса с ключом Authorization. Значение ключа в виде Token "ваш токен без ковычек".
Срок действия токена - 24 часа. Необходимо обновление по истечении срока (см.документацию)

### Документация проекта: :blue_book:
После запуска проекта (python3 manage.py runserver) документация со списком эндпоинтов доступна по ссылке:
http://localhost/api/docs/
