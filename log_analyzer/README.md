# Log Analyzer

CLI-утилита для анализа логов (.log/.txt).

## Возможности
- Подчет INFO/WARNING/ERROR
- TOP IP адресов
- TOP ERROR сообщений
- Фильтр по уровню '--level'
- Сохраниение отчетов в файл '--out'

## Запуск
'''bash
python loganalyzer.py sample.log

Фильтр по уровню:
python log_analizer.py sample.log --level ERROR

Сохранение отчета:
python log_analizer.py sample.lo --out report.txt

## ВАЖНО ПО БЕЗОПАСНОСТИ!

Тестируйте на копии логов, если файл содержит чувствительные данные.

