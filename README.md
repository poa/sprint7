# Sprint 7 final project. API Testing

## Общая информация

Проект содержит автотесты для API на базе `pytest` для сервиса [Yandex Scooter](https://qa-scooter.praktikum-services.ru/)

[Документация на API](https://qa-scooter.praktikum-services.ru/docs/). Неполная и содержит неточности

Тесты содержат allure-аннотации и перечень тестов можно посмотреть в отчёте allure (см. ниже)

## Запуск тестов и просмотр отчётов

* Установить зависимости 

    ```shell
    pip install -r requirements.txt.
    ```
* Для запуска тестов использовать следующую команду
 
    ```shell
    pytest -v
    ```
  
* Для запуска тестов с формированием отчёта allure использовать следующую команду
 
    ```shell
    pytest -v --alluredir=allure-results
    ```
  
* Для просмотра отчёта allure (allure предварительно должен быть [установлен](https://allurereport.org/docs/install/)) выполнить команду:

    ```shell
    allure serve allure-results
    ```
