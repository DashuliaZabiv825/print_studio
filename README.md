# Студия печати "Оттиск" (`print_studio`)

Веб-приложение из двух сервисов: витрина услуг на **Flask** и калькулятор стоимости на **FastAPI**.

## Тема и правило расчёта
- **Тема:** Студия печати (полиграфическая продукция на заказ).
- **Правило расчёта:** `итоговая_сумма = цена_услуги * количество` (количество — целое число от 1).
- **Пример расчёта:** Четыре открытки по 35 ₽ стоят **140 ₽**.

## Локальный запуск (без Docker)

### 1. Витрина на Flask
```bash
cd vitrina
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --port 500
```

### 2. Калькулятор на FastAPI
```bash
cd kalkulyator
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate
pip install -r requirements.txt
fastapi dev main.py --port 8000
```

## Запуск на сервере через Docker Compose
- **Каталог проекта:** `~/popova-print-studio`
- **Команда запуска:**
  ```bash
  docker compose up -d --build
  ```
- **Адреса на сервере (заполнить после деплоя):**
  - Витрина: ` http://192.168.1.11:20550`
  - Форма калькулятора: ` http://192.168.1.11:20551`
  - Документация API (`/docs`): ` http://192.168.1.11:20551/docs`
