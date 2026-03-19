# QA Auto Engineer Python Project 241

[![Actions Status](https://github.com/denginsf/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/denginsf/qa-auto-engineer-python-project-241/actions)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-241&metric=bugs)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-241) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-241&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-241) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=denginsf_qa-auto-engineer-python-project-241&metric=coverage)](https://sonarcloud.io/summary/new_code?id=denginsf_qa-auto-engineer-python-project-241)

Второй проект курса "Автоматизатор тестирования на Python" от Hexlet.  
**Gendiff** — это консольная утилита для поиска различий между двумя конфигурационными файлами. Проект демонстрирует понимание архитектуры Python-приложений, работу с древовидными структурами данных и реализацию нескольких форматов вывода.

## Возможности

- Поддержка **JSON** и **YAML** форматов (включая смешанные форматы)
- **Три формата вывода**:
  - `stylish` — древовидный, человекочитаемый формат с отступами
  - `plain` — построчный список изменений
  - `json` — машиночитаемый формат для интеграции с другими инструментами
- Рекурсивное сравнение вложенных структур любой глубины
- Гибкая архитектура с возможностью легкого добавления новых форматеров

## Тестирование

Как проект для автоматизатора тестирования, особое внимание уделил качеству кода и тестовому покрытию:

- **24 тестовых сценария**, покрывающих:
  - 3 форматера (stylish, plain, json)
  - 2 формата файлов (JSON, YAML с расширениями .yml/.yaml)
  - 4 варианта сравнения (полная дифф, пустой первый, пустой второй, оба пустые)
- **Pytest** — основной фреймворк для тестирования
- **Покрытие кода >85%** (отслеживается через SonarCloud)
- **Фикстуры** с тестовыми данными в отдельных директориях
- **Параметризация** тестов для разных форматов
- **TDD-подход** — тесты написаны до реализации функциональности
- **Непрерывная интеграция** — тесты запускаются автоматически при каждом пуше

## Демонстрация проекта

[![asciicast](https://asciinema.org/a/vhOky2ZrecQL1X2W.svg)](https://asciinema.org/a/vhOky2ZrecQL1X2W)