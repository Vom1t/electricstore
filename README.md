# ОНЛАЙН ПЛАТФОРМА ТОРГОВОЙ СЕТИ ЭЛЕКТРОНИКИ
## Тестовое задание

В данном проекте используются следующие модули:
* Django
* Postgresql
* Django Filter
* DRF


### Установка
### 1. Создать виртуальное окружение
```
python3 -m venv venv
```
#### Установить Poetry
```
# Установка
pip install poetry
```
```
# Установка зависимостей
poetry install
```

### 2. Подключить DB PostgreSQL

```
# Запуск образа Docker
docker-compose up --build -d
```
```
# Выполнить миграции
./manage.py migrate
```

### 5. Запустить сервер
```
./manage.py runserver
```