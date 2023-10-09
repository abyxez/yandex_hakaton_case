# yandex_hakaton_case
Web-service for Lenta shop.
Предназначен для анализа прогноза продаж товаров в сети магазинов Лента по всей России на основе модели предсказания.
Пользователи имеют возможность просматривать прогноз на 14 дней от текущей даты выбранного товара в выбранном магазине. Также можно смотреть анализировать продажи товаров и выводить расширенную статистику.


Технологии:
Python 3.9, Django 3.2, DRF 3.12, Nginx, Docker, Docker-compose, Postgresql

Порядок запуска на локальном компьютере: 
  Клонируйте репозиторий:
      git clone git@github.com:abyxez/yandex_hakaton_case.git
  Создайте и активируйте виртуальное окружение в папке backend, обновите pip и установите зависимости:
   - python -m venv venv
   - venv/Scripts/activate
   - python -m pip install --upgrade pip
   - python -r requirements.txt

  
   Создайте файл .env внутри папки  и внесите туда переменные окружения:
    SECRET_KEY
    ALLOWED_HOSTS
    SECRET_KEY=<КЛЮЧ>
    POSTGRES_USER=django_user
    POSTGRES_PASSWORD=mysecretpassword
    POSTGRES_DB=django
    DB_HOST=db
    DB_PORT=5432
   Запустите сборку контейнера:
    - docker-compose up -d --build
    Примените миграции, соберите статику и создайте суперпользователя:
    - docker-compose exec backend python manage.py makemigrations
    - docker-compose exec backend python manage.py migrate
    - docker-compose exec backend python manage.py collectstatic
    - docker-compose exec backend python manage.py createsuperuser
    Заполните базу :
    - скопируйте необходимые файлы в папку backend/data 
    - выполните команды в папке backend:
        - docker-compose exec backend python manage.py import_hash_id
        - docker-compose exec backend python manage.py import_csv
        - docker-compose exec backend python manage.py import_excel

Ресурсы API
Документация Api будет находится по адресу:


Порядок запуска на удаленном сервере:
  Клонируйте репозиторий:
   - git clone git@github.com:abyxez/foodgram-project-react.git
  Скопируйте из репозитория файлы, расположенные в директории backend:
    docker-compose.production.yml
    nginx.conf
 На сервере создайте директорию ;
 В директории foodgram создайте директорию  и поместите в неё файлы:
    docker-compose.production.yml
    nginx.conf
    .env со следующими данными:
        SECRET_KEY=<КЛЮЧ>
        POSTGRES_USER=django_user
        POSTGRES_PASSWORD=mysecretpassword
        POSTGRES_DB=django
        DB_HOST=db
        DB_PORT=5432
 В директории  следует выполнить команды:
    sudo docker compose -f docker-compose.production.yml up -d
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_hash_id
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_csv
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_excel

 Выполните команды:

    git add .
    git commit -m "Имя коммита"
    git push

 После этого будут запущены процессы workflow:

    проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
    сборка и доставка докер-образов для контейнеров frontend и backend на Docker Hub
    автоматический деплой проекта на сервер(копирование файлов docker-compose.production.yml и nginx.conf, создание миграций и сбор статики)


Проект доступен по ссылкам:
- 


Учетная запись администратора:
- почта:
- пароль: 
