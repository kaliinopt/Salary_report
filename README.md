# Python-скрипт для генерации отчетов о сотрудниках

Python-скрипт для генерации отчётов на основе CSV-файлов с данными сотрудников.

## Запуск 

```bash
python3 main.py data1.csv data2.csv --report payout
```

* data1.csv, data2.csv, ... — пути к CSV-файлам.

* --report payout - тип репорта либо payout, либо json_payout

## Поддержка новых отчётов

Чтобы добавить новый тип отчёта:

* Создайте новый класс в report.py, например class AverageHourlyRateReport.

* Реализуйте у него метод .generate(employees: List[Dict]) -> str.

* Зарегистрируйте его в функции get_report(report_type).

## Обработка ошибок

Скрипт сообщает о том когда:

* переданы несуществующие файлы,

* не указан --report,

* указан неизвестный тип отчёта.

## Пример отчетов

Console

Marketing
-------------------------------------------------------
Name                 |  Hours | Rate | Payout
-------------------------------------------------------
Alice Johnson        |  160.0 | $50.0 | $8000.00
Henry Martin         |  150.0 | $35.0 | $5250.00
-------------------------------------------------------
Total                |  310.0 |       | $13250.00

Design
-------------------------------------------------------
Name                 |  Hours | Rate | Payout
-------------------------------------------------------
Bob Smith            |  150.0 | $40.0 | $6000.00
Carol Williams       |  170.0 | $60.0 | $10200.00
-------------------------------------------------------
Total                |  320.0 |       | $16200.00

HR
-------------------------------------------------------
Name                 |  Hours | Rate | Payout
-------------------------------------------------------
Grace Lee            |  160.0 | $45.0 | $7200.00
Ivy Clark            |  158.0 | $38.0 | $6004.00
Liam Harris          |  155.0 | $42.0 | $6510.00
-------------------------------------------------------
Total                |  473.0 |       | $19714.00

Sales
-------------------------------------------------------
Name                 |  Hours | Rate | Payout
-------------------------------------------------------
Karen White          |  165.0 | $50.0 | $8250.00
Mia Young            |  160.0 | $37.0 | $5920.00
-------------------------------------------------------
Total                |  325.0 |       | $14170.00

Company Total ------------------------> $63334.00


Json
```json
{
  "type": "payout",
  "employees": [
    {
      "name": "Alice Johnson",
      "email": "alice@example.com",
      "department": "Marketing",
      "hours": 160.0,
      "rate": "50.0$",
      "payout": "8000.0$"
    },
    {
      "name": "Bob Smith",
      "email": "bob@example.com",
      "department": "Design",
      "hours": 150.0,
      "rate": "40.0$",
      "payout": "6000.0$"
    },
    {
      "name": "Carol Williams",
      "email": "carol@example.com",
      "department": "Design",
      "hours": 170.0,
      "rate": "60.0$",
      "payout": "10200.0$"
    },
    {
      "name": "Grace Lee",
      "email": "grace@example.com",
      "department": "HR",
      "hours": 160.0,
      "rate": "45.0$",
      "payout": "7200.0$"
    },
    {
      "name": "Henry Martin",
      "email": "henry@example.com",
      "department": "Marketing",
      "hours": 150.0,
      "rate": "35.0$",
      "payout": "5250.0$"
    },
    {
      "name": "Ivy Clark",
      "email": "ivy@example.com",
      "department": "HR",
      "hours": 158.0,
      "rate": "38.0$",
      "payout": "6004.0$"
    },
    {
      "name": "Karen White",
      "email": "karen@example.com",
      "department": "Sales",
      "hours": 165.0,
      "rate": "50.0$",
      "payout": "8250.0$"
    },
    {
      "name": "Liam Harris",
      "email": "liam@example.com",
      "department": "HR",
      "hours": 155.0,
      "rate": "42.0$",
      "payout": "6510.0$"
    },
    {
      "name": "Mia Young",
      "email": "mia@example.com",
      "department": "Sales",
      "hours": 160.0,
      "rate": "37.0$",
      "payout": "5920.0$"
    }
  ]
}
```

