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

