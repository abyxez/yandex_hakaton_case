# yandex_hakaton_case
Web-service for Lenta shop.
Предназначен для анализа прогноза продаж товаров в сети магазинов Лента по всей России на основе модели предсказания.
Пользователи имеют возможность просматривать прогноз на 14 дней от текущей даты выбранного товара в выбранном магазине. Также можно смотреть анализировать продажи товаров и выводить расширенную статистику.


Технологии:
Python 3.9, Django 3.2, DRF 3.12, Nginx, Docker, Docker-compose, Postgresql

Порядок запуска на локальном компьютере:

    Клонируйте репозиторий:
        - git clone git@github.com:abyxez/yandex_hakaton_case.git
    
    Создайте и активируйте виртуальное окружение в папке backend, обновите pip и установите зависимости:
        - python -m venv venv
        - venv/Scripts/activate
        - python -m pip install --upgrade pip
        - python -r requirements.txt

  
    Создайте файл .env внутри папки hakaton и внесите туда переменные окружения:

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
        - скопируйте необходимые файлы в папку hakaton/data 
        - выполните команды в папке backend:
            - docker-compose exec backend python manage.py import_hash_id
            - docker-compose exec backend python manage.py import_csv
            - docker-compose exec backend python manage.py import_excel

    Локальный запуск без docker-compose:
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py collectstatic
        - python manage.py createsuperuser
        - python manage.py import_hash_id
        - python manage.py import_import_csv
        - python manage.py import_import_excel
        - python manage.py runserver


Проект доступен по ссылкам:
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/api


Команда:

    - Константин Мельник(Старший backend-разработчик) 
    - Гулин Игорь(backend-разработчик)
    
