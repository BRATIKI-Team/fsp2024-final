# API 
Смотри API документацию по [/docs].

# Setup for Development
1. Для начала создайте виртуальное окружение:
```bash
python3 -m virtualenv venv
```
2. Инициализируйте виртуальное окружение:
```bash
./venv/Scripts/activate.bat
```
3. Установите зависимости проекта:
```bash
pip install -r requirements.txt
```
4. Скопируйте .env.local в .env.
5. Запустите веб-сервер:
```bash
uvicorn app.main:app --reload
```
