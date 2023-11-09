запустить контейнер с базой для теста:
```
docker run --name server -e POSTGRES_PASSWORD=demo -e POSTGRES_USER=demo -e POSTGRES_DB=core -d -p 5433:5432 postgres
```

запуск бека и установка зависимостей:
```sh
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r server/r.txt

python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com --noinput
python manage.py runserver
```

dev server run on: http://127.0.0.1:8000/

- admin/ админ-панель
- api/users/ регистрация
- api/login/ аутентификация
- answer/ точка входа для получения ответа от модели
