# Certificate Manager

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green)
![Poetry](https://img.shields.io/badge/Poetry-1.7.1-orange)
![Docker](https://img.shields.io/badge/Docker-24.0.5-blue)
![Nginx](https://img.shields.io/badge/Nginx-1.27.5-green)

## Описание

Сервис для проверки и автоматического обновления SSL-сертификатов на удалённых хостах (Debian), с web-интерфейсом и API на FastAPI. Проект структурирован по SOLID-принципам, поддерживает разные окружения и использует Poetry для управления зависимостями.

---

## Быстрый старт

### 1. Клонируйте репозиторий и установите зависимости

```sh
poetry install
```

### 2. Создайте переменные окружения

- Для production: `.env`
- Для разработки: `.env.dev`
- Для тестов: `.env.test`

**Пример содержимого:**
```
APP_NAME=Certificate Manager
DEBUG=True
ALLOWED_HOSTS=["*"]
LOG_LEVEL=DEBUG
CERTIFICATE_EXPIRY_DAYS=30
```

### 3. Запуск приложения

```sh
poetry run uvicorn app.main:app --reload
```

### 4. Запуск с разным окружением (Windows PowerShell)

- Для разработки:
  ```powershell
  $env:ENV="dev"; poetry run uvicorn app.main:app --reload
  ```
- Для тестов:
  ```powershell
  $env:ENV="test"; poetry run pytest
  ```
- Для продакшена (по умолчанию, если ENV не задан):
  ```powershell
  poetry run uvicorn app.main:app
  ```

---

## Тесты

```powershell
poetry run pytest
```

## Форматирование и линтинг

```powershell
poetry run black .
poetry run flake8
poetry run mypy .
```

---

## Структура проекта

- `app/` — исходный код приложения
  - `api/` — роуты FastAPI
  - `config/` — настройки и переменные окружения
  - `core/` — логирование и базовые утилиты
  - `models/` — pydantic-модели
  - `services/` — бизнес-логика
- `tests/` — тесты

---

## Использование Poetry

- Добавить зависимость: `poetry add <package>`
- Добавить dev-зависимость: `poetry add --group dev <package>`
- Добавить test-зависимость: `poetry add --group test <package>`
- Установить все зависимости: `poetry install`
- Запустить команду в окружении: `poetry run <command>`

---

## Переменные окружения

Для выбора файла переменных окружения используйте переменную `ENV`:

- Для разработки: `$env:ENV="dev"`
- Для тестов: `$env:ENV="test"`
- Для продакшена: не указывать (будет использован `.env`)

---

## Контакты

*iv.eruslanov@yandex.ru*
