# Log Analyzer (Python)

CLI-утилита для анализа лог-файлов.

## Возможности
- Подчет уровней логов (INFO / WARNING / ERROR)
- TOP IP-адресов
- TOP ERROR сообщений
- Фильтр по уровню '--level'
- Сохраниение отчёта в TXT или JSON

## Запуск
'''bash
python log_analyzer.py sample.log

Примеры:
python log_analizer.py sample.log --level ERROR
python log_analizer.py sample.log --top 5
python log_analizer.py sample.log --json-out report.json

## ВАЖНО ПО БЕЗОПАСНОСТИ!

Тестируйте на копии логов, если файл содержит чувствительные данные.

